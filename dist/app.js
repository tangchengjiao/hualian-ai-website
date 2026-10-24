const nav=document.querySelector('.nav');
const menu=document.querySelector('.menu-toggle');
menu?.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'关闭':'菜单';});
const dialog=document.querySelector('#wechat-dialog');
document.querySelectorAll('[data-contact]').forEach(button=>button.addEventListener('click',()=>dialog.showModal()));
dialog?.querySelector('.close').addEventListener('click',()=>dialog.close());
dialog?.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
function toast(message){let item=document.querySelector('.toast');if(!item){item=document.createElement('div');item.className='toast';item.role='status';document.body.append(item);}item.textContent=message;clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>item.remove(),3500);}
async function copy(text){try{await navigator.clipboard.writeText(text);toast('已复制，请到微信粘贴');}catch{toast('请长按复制：'+text);}}
document.querySelectorAll('[data-copy-wechat]').forEach(button=>button.addEventListener('click',()=>copy(document.body.dataset.wechat)));
const interest=document.querySelector('#interest');
if(interest){const requested=new URLSearchParams(location.search).get('service');if(requested){const option=[...interest.options].find(o=>o.value===requested);if(option)interest.value=requested;}}
document.querySelector('#copy-brief')?.addEventListener('click',()=>{const need=document.querySelector('#business-need').value.trim();copy(`见舟你好，我想了解华链 AI 的${interest.value}。${need?'\n我的业务需求：'+need:''}\n希望了解适合的服务方式、交付范围和完整报价。`);});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.textContent='菜单';menu.focus();}});
