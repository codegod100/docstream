<script>
  export let blips;
  export let counter;
  export let author;
  export let callback;
  export let updateAuthors;
  export let stringToColor;
  export let locked;
  export let authors;
  export let io;
  import Mine from "$lib/Mine.svelte";
  import Theirs from "$lib/Theirs.svelte";
  console.log("AUTHORS", authors);
  let mounted = false;
  let count = 0;

  let next = counter + 1;
  async function addBlip(i) {
    let blip = blips[i];
    let endpoint = `http://localhost:5000/add/${blip.id}`;
    let blipData = { content: "edit me", author };
    let resp = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(blipData),
    });
    let id = await resp.json();
    console.log("created id: ", id);
    blips[i].blips = [
      {
        id,
        count,
        blips: [],
        content: "<div>edit me</div>",
        author,
        color: stringToColor(author),
      },
      ...blips[i].blips,
    ];
    count++;
  }
  for (const blip of blips) {
    if (authors) {
      authors = authors.add(blip.author);
      console.log("AUTH", authors);
    }
  }
</script>

{#each blips as blip, i}
  {#if blip.author == author}
    <Mine {blip} {counter} {io} />
  {:else}
    <Theirs {blip} {counter} />
  {/if}

  {#if blip.blips}
    <svelte:self blips={blip.blips} counter={next} bind:authors {author} {io} />
  {/if}
{/each}
