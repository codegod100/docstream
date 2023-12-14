<script>
  import { stringToColor } from "$lib/common.js";
  export let blip;
  export let counter;
  let color = stringToColor(blip.author);
  let margin = counter * 5;
</script>

<div
  role="button"
  data-author={blip.author}
  data-id={blip.id}
  style="background-color: {color}; margin-left: {margin}px"
>
  {@html blip.content}
</div>
