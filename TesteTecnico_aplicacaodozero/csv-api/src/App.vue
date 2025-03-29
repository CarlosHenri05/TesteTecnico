<template>
  <div class="container mx-auto px-4 py-10">
    <div class="max-w-3xl mx-auto">
      <div class="text-center mb-10">
        <h1 class="text-3xl font-bold text-gray-800 mb-2">Pesquisa de Dados CSV</h1>
        <p class="text-gray-600">Digite uma palavra-chave para filtrar os dados do relatório CADOP</p>
      </div>

      <SearchForm :isLoading="isLoading" @searchSubmit="searchData" />

      <div v-if="isLoading" class="text-center my-10">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-4 border-gray-300 border-t-blue-600"></div>
        <p class="mt-2 text-gray-600">Carregando resultados...</p>
      </div>

      <ResultsTable v-else-if="results && results.length > 0" :results="results" :headers="headers" />

      <div v-else-if="searched" class="text-center py-10 bg-white rounded-lg shadow-lg">
        <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="mt-2 text-sm font-medium text-gray-900">Nenhum resultado encontrado</h3>
        <p class="mt-1 text-sm text-gray-500">Tente uma palavra-chave diferente para sua pesquisa.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchForm from './components/SearchForm.vue'
import ResultsTable from './components/ResultsTable.vue'

export default {
  name: 'App',
  components: {
    SearchForm,
    ResultsTable,
  },
  data() {
    return {
      results: [],
      headers: [],
      isLoading: false,
      searched: false,
    }
  },
  methods: {
    async searchData(keyword) {
      if (!keyword || !keyword.trim()) {
        return
      }

      this.isLoading = true
      this.searched = true

      try {
        const response = await axios.get('http://localhost:5000/search', {
          params: {
            keyword: keyword,
          },
        })

        if (response.data && response.data.results) {
          this.results = response.data.results
          this.headers = response.data.headers || []
        } else {
          console.error('Formato de resposta inesperado:', response.data)
          this.results = []
          this.headers = []
        }
      } catch (error) {
        console.error('Erro ao buscar dados:', error)
        this.results = []
        this.headers = []
      } finally {
        this.isLoading = false
      }
    },
  },
}
</script>
