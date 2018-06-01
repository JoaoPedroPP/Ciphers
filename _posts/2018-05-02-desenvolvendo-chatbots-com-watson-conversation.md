---
ID: 13505
post_title: >
  Desenvolvendo Chatbots com Watson
  Conversation
author: Marcelo Strogenski
post_excerpt: ""
layout: post
permalink: >
  http:/\/169.57.188.51:30180/2018/05/02/desenvolvendo-chatbots-com-watson-conversation/
published: true
post_date: 2018-05-02 10:25:25
---
<div class="section-inner sectionLayout--insetColumn">
<h4 id="983e" class="graf graf--h4 graf-after--figure"><strong class="markup--strong markup--h4-strong">Mas o que é "esse Watson"?</strong></h4>
<p id="0564" class="graf graf--p graf--hasDropCapModel graf--hasDropCap graf-after--h4"><span class="graf-dropCap">P</span>ara falar de Watson vale um breve histórico: o Watson foi lançado em <strong class="markup--strong markup--p-strong">2011</strong> e em sua primeira aparição no <strong class="markup--strong markup--p-strong">Jeopardy</strong>, ganhando de dois super especialistas do jogo. Posteriormente, com muito estudo e desenvolvimento, o Watson tornou-se <strong class="markup--strong markup--p-strong">APIs</strong> disponíveis na <a class="markup--anchor markup--p-anchor" href="http://bluemix.net/" target="_blank" rel="nofollow noopener" data-href="http://bluemix.net/"><strong class="markup--strong markup--p-strong">IBM Cloud.</strong></a></p>
<p class="graf graf--p graf--hasDropCapModel graf--hasDropCap graf-after--h4">O Watson Conversation, especificamente, trata-se de uma <strong class="markup--strong markup--blockquote-strong">API para desenvolvimento de Bots</strong>, com uma <strong class="markup--strong markup--blockquote-strong">interface simples</strong> para que até mesmo uma pessoa que não seja de TI consiga desenvolver e ensinar conteúdo ao bot.</p>

<h3 id="0778" class="graf graf--h3 graf-after--blockquote"><strong class="markup--strong markup--h3-strong">O que faremos aqui?</strong></h3>
<p id="4c46" class="graf graf--p graf-after--h3 graf--trailing">Feitas as devidas apresentações, neste tutorial faremos um chatbot para pedido de pizza! Nesse caso, <strong class="markup--strong markup--p-strong">mais importante do que o tema do Bot é o entendimento da interface do Watson Conversation</strong>. O tutorial ficou um pouco longo pois explicarei cada parte da API, qualquer dúvida só comentar ok?</p>

</div>
&nbsp;
<h3 id="cc12" class="graf graf--h3 graf--leading"><strong class="markup--strong markup--h3-strong">Criando a API:</strong></h3>
<p id="e85e" class="graf graf--p graf-after--h3">Para criar a API você precisa criar uma conta na <a class="markup--anchor markup--p-anchor" href="https://console.bluemix.net/" target="_blank" rel="nofollow noopener" data-href="https://console.bluemix.net/">IBM Cloud</a> a qual te dará acesso à diversos serviços tanto de Watson como de Infra e Plataforma para sempre!! ( não , <strong class="markup--strong markup--p-strong">você não terá que colocar o seu cartão de crédito ao utilizar a camada free</strong>).</p>
<p id="4d85" class="graf graf--p graf-after--p">Pois bem, com a conta criada você terá que ir no catálogo e lá no final da página selecionar o serviço de Conversation:</p>
<img class="alignnone size-full wp-image-13533" src="http://bluedev.com.br/wp-content/uploads/2018/05/Imagem-2.png" alt="" width="800" height="445" />
<p id="fe00" class="graf graf--p graf-after--figure">Após clicar em Create, você será direcionado à página do Conversation. É legal saber que neste caso trabalharemos com o <strong class="markup--strong markup--p-strong">Toolkit</strong> mas é possível fazer o desenvolvimento na mão com os <a class%3