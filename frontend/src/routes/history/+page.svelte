<script>
  let history = [];
  let error = '';

  // Fetch history when page loads
  onMount(async () => {
    try {
      const res = await fetch('https://address-mapping.onrender.com/history');
      if (!res.ok) throw new Error('Failed to fetch history');
      history = await res.json();
    } catch (err) {
      error = err.message;
    }
  });

  import { onMount } from 'svelte';
</script>

<h1>Distance Calculator</h1>
<p>Prototype web application for calculating the distance between addresses.</p>

<div class="history-card">
  <div class="header-row">
    <h2>Historical Queries</h2>
    <a href="/" class="back-button">Back to Calculator 🔙</a>
  </div>

  {#if error}
    <p class="error">❌ {error}</p>
  {:else if history.length === 0}
    <p>No historical data found.</p>
  {:else}
    <table>
      <thead>
        <tr>
          <th>Source Address</th>
          <th>Destination Address</th>
          <th>Distance in Miles</th>
          <th>Distance in Kilometers</th>
        </tr>
      </thead>
      <tbody>
        {#each history as item}
          <tr>
            <td>{item.source}</td>
            <td>{item.destination}</td>
            <td>{item.miles} mi</td>
            <td>{item.kilometers} km</td>
          </tr>
        {/each}
      </tbody>
    </table>
  {/if}
</div>

<style>
  .history-card {
    max-width: 1000px;
    margin: 2rem auto;
    padding: 2rem;
    background: #f9f9f9;
    border-radius: 10px;
  }

  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
  }

  th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #ccc;
  }

  th {
    background-color: #eee;
  }

  .back-button {
    background: #333;
    color: white;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
  }

  .back-button:hover {
    background: #555;
  }

  .error {
    color: red;
    font-weight: bold;
  }
</style>
