<script>
  import { stringToColor } from "$lib/common.js";
  export let counter;
  export let io;
  export let blip;
  let color = stringToColor(blip.author);
  let margin = counter * 5;
</script>

<div
  data-author={blip.author}
  data-id={blip.id}
  style="background-color: {color}; margin-left: {margin}px"
  contenteditable="true"
  on:blur={async (event) => {
    let endpoint = `http://localhost:5000/edit/${blip.id}`;
    let data = { content: event.target.innerHTML };
    await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    io.emit("content", "ok");
  }}
>
  {@html blip.content}
</div>
