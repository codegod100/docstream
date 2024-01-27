<script>
  export let counter;
  export let io;
  export let blip;
  export let colorMap;
  let margin = counter * 5;
  import { onMount, afterUpdate, beforeUpdate } from "svelte";
  // beforeUpdate(() => {
  //   let element = document.getElementById(blip.id);
  //   if (element) {
  //     element.innerHTML = "";
  //     const fixed = fixBrokenHTML(blip.content);
  //     element.innerHTML = fixed;
  //   }
  // });
  afterUpdate(() => {
    if (blip.focus) {
      document.getElementById(blip.id)?.focus();
    }

    let element = document.getElementById(blip.id);
    if (element) {
      element.innerHTML = "";
      const fixed = fixBrokenHTML(blip.content);
      element.innerHTML = fixed;
    }
  });

  function fixBrokenHTML(brokenHTML) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(brokenHTML, "text/html");
    return doc.documentElement.innerHTML;
  }
</script>

<div class="flex" style="padding-left: {margin}px">
  <div
    class="grow"
    id={blip.id}
    role="textbox"
    tabindex="0"
    data-author={blip.author}
    data-id={blip.id}
    style="background-color: {colorMap[blip.author]};"
    contenteditable="true"
    on:blur={async (event) => {
      let endpoint = `/edit/${blip.id}`;
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
    {@html blip.content}
  </div>
  <button
    class="bg-red-500 btn btn-blue w-50px"
    on:click={async () => {
      let endpoint = `/remove/${blip.id}`;
      await fetch(endpoint, {
        method: "POST",
      });
      io.emit("content", "ok");
    }}>[ X ]</button
  >
</div>
