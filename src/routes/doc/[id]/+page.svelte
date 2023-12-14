<script>
  import Blip from "$lib/Blip.svelte";
  import { stringToColor } from "$lib/common.js";
  export let data;
  const author = data.author;
  let blips = [data.json];

  $: authors = new Set([author]);
  $: locked = false;
  console.log("LOADING PAGE");
  let slug = data.id;
  let io = data.io;
  // setInterval(async () => {
  //   console.log("grabbing data");
  //   blips = [await data.renew()];
  // }, 5000);

  io.on("content", async () => {
    console.log("grabbing data");
    blips = [await data.renew()];
  });
</script>

<div style="background-color: {stringToColor(author)}">
  Current Author: {author}
</div>
<div>
  Authors:
  {#each authors as author}
    <span style="background-color: {stringToColor(author)}">[ {author} ]</span>
  {/each}
</div>

<Blip
  {blips}
  counter={1}
  {author}
  {locked}
  {slug}
  {io}
  bind:authors
  callback={async (blip) => {}}
/>
