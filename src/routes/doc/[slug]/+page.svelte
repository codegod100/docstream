<script>
  import Blip from "$lib/Blip.svelte";
  import { stringToColor } from "$lib/common.js";
  import ioClient from "socket.io-client";
  const io = ioClient(`http://localhost:5000`);
  export let data;
  const author = data.author;
  let blips = [data.json];
  let authors = new Set([author]);

  io.on("content", async () => {
    let slug = data.slug;
    let endpoint = `http://localhost:5000/doc/${slug}`;
    let resp = await fetch(`${endpoint}?author=${author}`);
    let json = await resp.json();
    blips = [json];
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
