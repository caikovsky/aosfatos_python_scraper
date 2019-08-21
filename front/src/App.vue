<template>
  <div id="app" class="container-fluid">

    <!-- Header -->
		<b-row class="justify-content-center text-center mt-5 mb-5">
			<b-col md="12">
				<h1>Lista de fatos - AosFatos.org</h1>
			</b-col>
		</b-row>

    <!-- Fatos table -->
    <DataTable />
  </div>
</template>

<script>
import DataTable from './components/DataTable.vue'

export default {
  name: 'app',
  components: {
    DataTable
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
