<template>
	<div>
		<!-- List -->
		<b-row class="justify-content-center">
			<b-col md="12">
				<b-table
					bordered
					hover
					:items="items"
					:fields="fields"
					:busy="isLoading"
					per-page="10"
					:current-page="currentPage"
				>
					<div
						slot="table-busy"
						class="text-center text-danger my-2"
					>
						<b-spinner class="align-middle"></b-spinner>
					</div>

					<div
						slot="actions"
						slot-scope="row"
						class="text-center"
					>
						<b-button
							size="sm"
							:href="`${row.item.url}`"
							class="text-center btn-ghost-primary"
							target="_blank"
						>Ver</b-button>
					</div>
				</b-table>

				<b-row>
					<b-col
						md="12"
						class="my-1"
					>
						<b-pagination
							v-model="currentPage"
							:total-rows="totalRows"
							:per-page="perPage"
							class="justify-content-center my-0"
						></b-pagination>
					</b-col>
				</b-row>
			</b-col>
		</b-row>
	</div>
</template>

<script>
export default {
	name: "DataTable",
	mounted() {
		this.$http
			.get(`http://localhost:5000/api/crawl`)
			.then(response => {
				this.items = response.data;
				this.totalRows = this.items.length;
				this.toggleLoading();
			})
			.catch(error => {
				console.error(error);
				this.toggleLoading();
			});
	},
	data() {
		return {
			isLoading: true,
			fields: [
				{ key: "quote_text", label: "Fato", sortable: true },
				{ key: "status", label: "Real?", sortable: true },
				{ key: "actions", label: "Ações", sortable: false }
			],
			items: [],
			currentPage: 1,
			perPage: 10,
			totalRows: 0
		};
	},
	methods: {
		toggleLoading() {
			this.isLoading = !this.isLoading;
		}
	}
};
</script>

<style scoped>
</style>
