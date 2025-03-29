<template>
  <div class="bg-white rounded-lg shadow-lg overflow-hidden">
    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th v-for="(header, index) in headers" :key="index" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              {{ header }}
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="(row, rowIndex) in results" :key="rowIndex">
            <td v-for="(cell, cellIndex) in row" :key="cellIndex" class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              {{ cell }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultsTable',
  props: {
    results: {
      type: Array,
      required: true,
    },
    headers: {
      type: Array,
      required: true,
    },
  },
}
</script>
