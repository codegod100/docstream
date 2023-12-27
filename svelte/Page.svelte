<script>
  import Blip from "./Blip.svelte";
  import { stringToColor } from "./common.js";
  import ioClient from "socket.io-client";
  const io = ioClient(`/`);
  export let author;
  export let blips;
  export let slug;
  console.log("AUTHOR", author);
  console.log("BLIPS", blips);

  // let blips = [data.json];
  let authors = new Set([author]);

  io.on("content", async () => {
    let endpoint = `/doc/${slug}`;
    let resp = await fetch(`${endpoint}?author=${author}`);
    let json = await resp.json();
    blips = [json];
  });
  import { onMount } from "svelte";
  console.log("raw log");
  onMount(() => {
    console.log("loading page");
  });
</script>

<div style="background-color: {stringToColor(author)}">
  Current Author: {author}
</div>
<div>
  Authors:
  {#each authors as a}
    <span style="background-color: {stringToColor(a)}">[&nbsp;{a}&nbsp;]</span>
  {/each}
</div>

<Blip {blips} counter={1} {author} {io} bind:authors />
