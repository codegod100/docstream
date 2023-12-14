<script>
  import Blip from "$lib/Blip.svelte";
  export let data;
  const author = data.author;
  let blippy = [data.json];
  function stringToColor(str) {
    let hash = 5381;
    for (let i = 0; i < str.length; i++) {
      hash = (hash << 5) + hash + str.charCodeAt(i); /* hash * 33 + c */
      // console.log("hash", hash);
    }
    let golden_ratio = 0.618033988749895;
    let hue = Math.abs(((hash * golden_ratio) % 1) * 360);
    // console.log("hue", hue);
    return `hsl(${hue}, 50%,  70%)`;
  }

  $: blips = blippy;
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

<div>Current Author: {author}</div>
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
  {stringToColor}
  updateAuthors={(author) => {
    authors.add(author);
    authors = authors;
  }}
  callback={async (blip) => {
    let endpoint = `http://localhost:5000/edit/${blip.id}`;
    let blipData = { content: blip.content };
    await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(blipData),
    });
    io.emit("content", "ok");
  }}
/>
