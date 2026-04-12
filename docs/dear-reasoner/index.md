---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "致未来的推理科学家"
  text: "让推理科学真正属于每一个人"
  image:
    src: /cover_minimal_letters.svg
    alt: Datawhale开源教程
  actions:
    - theme: brand
      text: 开始学习
      link: /dear-reasoner/volume1/chapter1/

features:
  - title: 🌐 开源
    details: 教程和文件全部托管在GitHub
---
<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/lizixi-0x2f.png',
    name: '李籽溪',
    title: '编辑/作者',
    links: [
      { icon: 'github', link: 'https://github.com/lizixi-0x2f' },
    ]
  },
]
</script>


<h2 align="center">Team</h2>
<VPTeamMembers size="small" :members />