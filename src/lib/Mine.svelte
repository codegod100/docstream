<script>
  import { stringToColor } from "$lib/common.js";
  export let counter;
  export let io;
  export let blip;
  let color = stringToColor(blip.author);
  let margin = counter * 5;
  import { onMount, afterUpdate, beforeUpdate } from "svelte";
  beforeUpdate(() => {
    let element = document.getElementById(blip.id);
    if (element) {
      element.innerHTML = "";
      element.innerHTML = blip.content;
    }
  });
  afterUpdate(() => {
    console.log("blip content", blip.content);
    if (blip.focus) {
      document.getElementById(blip.id)?.focus();
    }
  });
</script>

<div class="grid grid-cols-10 grid-flow-row" style="padding-left: {margin}px">
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
    id={blip.id}
    role="textbox"
    tabindex="0"
    class="col-span-9"
    data-author={blip.author}
    data-id={blip.id}
    style="background-color: {color}; "
    contenteditable="true"
    on:blur={async (event) => {
      let endpoint = `http://localhost:5000/edit/${blip.id}`;
      let data = { content: event.target.innerHTML };
      // event.target.innerHTML = "";
      await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      io.emit("content", "ok");
    }}
    on:keydown={(e) => {
      if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
        document.activeElement.blur();
      }
    }}
  >
    {blip.content}
  </div>
</div>
