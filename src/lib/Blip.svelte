<script>
  export let blips;
  export let counter;
  export let author;
  export let callback;
  export let updateAuthors;
  export let stringToColor;
  export let locked;
  export let slug;

  for (let blip of blips) {
    // console.log("grabbing color");
    blip.color = stringToColor(blip.author);
    updateAuthors(blip.author);
  }

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
        blips: [],
        content: "<div>edit me</div>",
        author,
        focus: "autofocus",
        color: stringToColor(author),
      },
      ...blips[i].blips,
    ];
  }
</script>

{#each blips as blip, i}
  {(blip.color = stringToColor(blip.author)) && ""}
  {#if blip.author == author}
    <div
      data-author={blip.author}
      data-id={blip.id}
      contenteditable="true"
      on:blur={() => {
        locked = false;
        // blip.html = "";
        blip.content = blip.editable.innerHTML;
        callback(blip);
      }}
      on:focus={() => {
        locked = true;
      }}
      bind:this={blip.editable}
      style="background-color: {blip.color}; margin-left: {counter * 5}px"
    >
      {@html blip.content}
    </div>
  {:else}
    <div
      data-author={blip.author}
      data-id={blip.id}
      role="button"
      on:click={() => addBlip(i)}
      style="background-color: {blip.color}; margin-left: {counter * 5}px"
    >
      {@html blip.content}
    </div>
  {/if}

  {#if blip.blips}
    <svelte:self
      blips={blip.blips}
      counter={next}
      {author}
      {updateAuthors}
      {stringToColor}
      {callback}
      {locked}
      {slug}
    />
  {/if}
{/each}
