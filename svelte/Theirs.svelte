<script>
  export let blip;
  export let counter;
  export let author;
  export let colorMap;

  let margin = counter * 5;

  async function addBlip() {
    for (const b of blip.blips) {
      if (b.author == author) {
        // only one blip child per author for now
        return;
      }
    }
    let endpoint = `/add/${blip.id}`;
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
  title={blip.author}
  role="button"
  tabindex="0"
  data-author={blip.author}
  data-id={blip.id}
  style="background-color: {colorMap[blip.author]}; margin-left: {margin}px"
  on:click={addBlip}
>
  {@html blip.content}
</div>
