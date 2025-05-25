<script>
  // Add if you need layout-level logic
</script>

<svelte:head>
  <!-- ✅ Google Fonts for headings and body text -->
  <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Montserrat:wght@600&display=swap"
  />
  <title>Distance Calculator</title>
</svelte:head>

<!-- ✅ Page wrapper to center content -->
<div class="app-container">
  <slot />
</div>

<style global>
  /* ✅ Global font and background */
  body {
    margin: 0;
    padding: 0;
    font-family: 'Open Sans', sans-serif;
    background-color: #f5f5f5;
    color: #333;
  }

  h1, h2 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    margin-bottom: 1rem;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  button {
    font-family: 'Open Sans', sans-serif;
  }
</style>

<style>
  /* ✅ Optional content container (centered layout) */
  .app-container {
    min-height: 100vh;
    max-width: 960px;
    margin: 0 auto;
    padding: 2rem 1rem;
  }
</style>
