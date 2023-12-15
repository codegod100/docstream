<script>
  import { stringToColor } from "$lib/common.js";
  export let blip;
  export let counter;
  export let author;
  let color = stringToColor(blip.author);
  let margin = counter * 5;

  async function addBlip() {
    for (const b of blip.blips) {
      if (b.author == author) {
        // one one blip child per author for now
        console.log("already have blip member");
        return;
      }
    }
    let endpoint = `http://localhost:5000/add/${blip.id}`;
    let content = "";
    let blipData = { content, author };
    let resp = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(blipData),
    });
    let id = await resp.json();
    console.log("created id: ", id);

    blip.blips = [
      ...blip.blips,
      {
        id,
        blips: [],
        content,
        author,
        focus: true,
      },
    ];
  }
</script>

<div
  role="button"
  data-author={blip.author}
  data-id={blip.id}
  style="background-color: {color}; margin-left: {margin}px"
  on:click={addBlip}
>
  {@html blip.content}
</div>
