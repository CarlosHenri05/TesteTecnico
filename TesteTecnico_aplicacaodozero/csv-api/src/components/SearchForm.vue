<template>
  <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
    <div class="flex flex-col md:flex-row md:items-end space-y-4 md:space-y-0 md:space-x-4">
      <div class="flex-grow">
        <label for="keyword" class="block text-sm font-medium text-gray-700 mb-1">Palavra-chave</label>
        <input
          type="text"
          id="keyword"
          v-model="keyword"
          @keyup.enter="submitSearch"
          class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          placeholder="Digite para pesquisar..."
        />
      </div>
      <div>
        <button
          @click="submitSearch"
          class="w-full md:w-auto px-6 py-2 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
          :disabled="isLoading"
        >
          <span v-if="isLoading">Pesquisando...</span>
          <span v-else>Pesquisar</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchForm',
  props: {
    isLoading: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      keyword: '',
    }
  },
  methods: {
    submitSearch() {
      this.$emit('searchSubmit', this.keyword)
    },
  },
}
</script>
