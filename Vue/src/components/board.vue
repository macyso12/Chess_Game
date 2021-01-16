<template>
    <div class="board">
        <span v-for="row in 8" :key="row">
            <span v-for="col in 8" :key="col">
                <span class="row">
                    <span v-if="(row+col)%2==0">
                        <img src="@/assets/bord.png" />
                    </span>
                    <span v-else>
                        <img src="@/assets/word.jpg" />
                    </span>
                </span>
            </span>
        </span>
    </div>
</template>

<script>

export default {
    name: 'board',
}
</script>


<style>
    .board {
        display: grid;
        grid-template-columns: repeat(8, minmax(4, 4fr));
        max-width: 300rem;
        margin: 5rem auto;
        padding: 0 5rem;
    }

    .row img {
        resize: 30%;
        width: 4vw;
        height: 4vw;
        object-fit: cover;
        crop: "fill";
    }
</style>