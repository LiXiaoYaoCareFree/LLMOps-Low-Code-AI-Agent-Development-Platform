<script setup lang="ts">
import { post } from '@/utils/request'

async function debug() {
  const response = await post('/apps/f5778a2a-9d68-48c6-9c49-7c2c25d54d0d/debug', {
    body: { query: '你好，你是谁' },
  })
  console.log(response)
}
</script>

<template>
  <a-button @click="debug">发起请求</a-button>
</template>

<style scoped></style>
