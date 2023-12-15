<script>
  import { stringToColor } from "$lib/common.js";
  export let counter;
  export let io;
  export let blip;
  let color = stringToColor(blip.author);
  let margin = counter * 5;
</script>

<div class="grid grid-cols-10 grid-flow-row" style="margin-left: {margin}px">
  <button
    class="bg-red-500 btn btn-blue"
    on:click={async () => {
      let endpoint = `http://localhost:5000/remove/${blip.id}`;
      await fetch(endpoint, {
        method: "POST",
      });
      io.emit("content", "ok");
    }}>[ X ]</button
  >
  <div
    class="col-span-9"
    data-author={blip.author}
    data-id={blip.id}
    style="background-color: {color}; "
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
</div>
