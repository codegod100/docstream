<script>
  export let blips;
  export let counter;
  export let author;
  export let authors;
  export let colorMap;
  export let io;
  import Mine from "./Mine.svelte";
  import Theirs from "./Theirs.svelte";
  import { onMount, afterUpdate } from "svelte";
  import { convertKeys } from "./common";
  // blips = convertKeys(blips);
  let next = counter + 1;

  afterUpdate(() => {
    for (const blip of blips) {
      if (authors) {
        authors = authors.add(blip.author);
      }
    }
  });
</script>

{#each blips as blip, i}
  {#if blip.author == author}
    <Mine {blip} {counter} {colorMap} {io} />
  {:else}
    <Theirs {counter} {colorMap} bind:blip {author} />
  {/if}

  {#if blip.blips}
    <svelte:self
      blips={blip.blips}
      {colorMap}
      counter={next}
      bind:authors
      {author}
      {io}
    />
  {/if}
{/each}
