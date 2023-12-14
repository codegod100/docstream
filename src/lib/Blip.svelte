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

  for (const blip of blips) {
    if (authors) {
      authors = authors.add(blip.author);
    }
  }
</script>

{#each blips as blip, i}
  {#if blip.author == author}
    <Mine {blip} {counter} {io} />
  {:else}
    <Theirs {counter} bind:blip {author} />
  {/if}

  {#if blip.blips}
    <svelte:self blips={blip.blips} counter={next} bind:authors {author} {io} />
  {/if}
{/each}
