<template>
    <span class="row">
        <span v-if="({{row}}+{{col}})%2==0">
            <img src="@/assets/bord.png" />
        </span>
        <span v-else>
            <img src="@/assets/word.jpg" />
        </span>
    </span>
</template>

<script>
    export default {
        name: 'chessSquare',
        props: {
            row: Number,
            col: Number
            total = row+col
        }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .square img {
        width: 100%;
        height: 3vw;
        object-fit: cover;
    }
</style>
