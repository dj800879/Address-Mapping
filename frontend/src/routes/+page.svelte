<script lang="ts">
  let source: string = '';
  let destination: string = '';
  let unit: 'miles' | 'kilometers' | 'both' = 'kilometers';
  let distanceKm: number | null = null;
  let distanceMi: number | null = null;
  let error: string = '';

  async function calculateDistance(): Promise<void> {
    error = '';
    distanceKm = null;
    distanceMi = null;

    try {
      const response = await fetch('https://address-mapping.onrender.com/distance', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ source, destination })
      });

      if (!response.ok) throw new Error('Distance calculation failed');

      const data = await response.json();
      distanceKm = data.kilometers;
      distanceMi = data.miles;
    } catch (err) {
      error = '❌ ' + ((err as Error).message || 'Something went wrong');
    }
  }
</script>

<h1>Distance Calculator</h1>

<div class="card">
  <form on:submit|preventDefault={calculateDistance} class="form">
    <label>
      Source Address
      <input bind:value={source} required placeholder="Enter source" />
    </label>
    <label>
      Destination Address
      <input bind:value={destination} required placeholder="Enter destination" />
    </label>

    <div class="unit-options">
      <label><input type="radio" bind:group={unit} value="miles" /> Miles</label>
      <label><input type="radio" bind:group={unit} value="kilometers" /> Kilometers</label>
      <label><input type="radio" bind:group={unit} value="both" /> Both</label>
    </div>

    <button type="submit" class="calculate-btn">Calculate Distance 🧮</button>
  </form>

  {#if distanceKm !== null && distanceMi !== null}
    <div class="result">
      {#if unit === 'miles'}
        <p><strong>{distanceMi} mi</strong></p>
      {:else if unit === 'kilometers'}
        <p><strong>{distanceKm} km</strong></p>
      {:else}
        <p><strong>{distanceMi} mi</strong> | <strong>{distanceKm} km</strong></p>
      {/if}
    </div>
  {/if}

  {#if error}
    <div class="error">{error}</div>
  {/if}

  <div class="history-link-container">
    <a href="/history" class="history-link">View Historical Queries 🔄</a>
  </div>
</div>

<style>
  h1 {
    text-align: center;
    margin-top: 1.5rem;
  }

  .card {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: #f3f3f3;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  input {
    padding: 0.75rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 1rem;
    width: 100%;
  }

  .unit-options {
    display: flex;
    justify-content: space-around;
    margin-top: 1rem;
  }

  .calculate-btn {
    margin-top: 1.5rem;
    background-color: red;
    color: white;
    border: none;
    padding: 0.75rem;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
  }

  .calculate-btn:hover {
    background-color: #c70000;
  }

  .result {
    margin-top: 1rem;
    font-size: 1.2rem;
    text-align: center;
    font-weight: bold;
  }

  .error {
    color: red;
    margin-top: 1rem;
    font-weight: bold;
    text-align: center;
  }

  .history-link-container {
    text-align: center;
    margin-top: 2rem;
  }

  .history-link {
    text-decoration: none;
    background: #333;
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 5px;
    display: inline-block;
  }

  .history-link:hover {
    background-color: #555;
  }
</style>