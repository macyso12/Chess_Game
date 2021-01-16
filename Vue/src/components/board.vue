<template>
    <div class="board">
        <span v-for="row in 8" :key="row">
            <span v-for="col in 8" :key="col">
                <chessSquare v-bind:row="row" v-bind:col="col" />
            </span>
        </span>
    </div>
</template>

<script>
    import chessSquare from './chessSquare.vue'
export default {
    name: 'board',
    components: {
        chessSquare
    }
}
</script>


<style>
    .board {
        display: grid;
        grid-gap: 0;
        grid-template-columns: repeat(8);
        grid-template-rows: auto;
        grid-auto-flow: row;
    }

</style>