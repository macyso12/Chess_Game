<template>
    <span class="square">
        <span v-if="(row+col)%2==0" @click="clickMethod(row,col)">
            <img src="@/assets/bord.png" />
        </span>
        <span v-else>
            <img src="@/assets/word.jpg" @click="clickMethod(row,col)"/>
        </span>
    </span>
</template>

<script>
    export default {
        name: 'chessSquare',
        props: {
            row: Number,
            col: Number
        },
        methods: {
            clickMethod(row,col) {
                console.log("Square is at row: "+row+" col: "+col)
            }
        }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .square img {
        width: 4vw;
        height: 4vw;
        object-fit: cover;
        grid-row-gap: 0;
    }
</style>
