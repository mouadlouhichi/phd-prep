
(function(){
  var input=document.getElementById('q');
  var hit=document.getElementById('hits');
  if(!input) return;
  function mark(root,term){
    if(!term) return 0;
    var walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null);
    var nodes=[],n,c=0;
    while(n=walker.nextNode()){ if(/\S/.test(n.nodeValue) && n.nodeValue.toLowerCase().indexOf(term)>=0) nodes.push(n); }
    nodes.forEach(function(node){
      var idx=node.nodeValue.toLowerCase().indexOf(term), frag=document.createDocumentFragment(), last=0;
      while(idx>=0){
        frag.appendChild(document.createTextNode(node.nodeValue.slice(last,idx)));
        var m=document.createElement('mark'); m.textContent=node.nodeValue.substr(idx,term.length);
        frag.appendChild(m); c++; last=idx+term.length; idx=node.nodeValue.toLowerCase().indexOf(term,last);
      }
      frag.appendChild(document.createTextNode(node.nodeValue.slice(last)));
      node.parentNode.replaceChild(frag,node);
    });
    return c;
  }
  var timer=null;
  function run(){
    var term=(input.value||'').trim().toLowerCase();
    document.querySelectorAll('mark').forEach(function(m){m.replaceWith(document.createTextNode(m.textContent));});
    if(term.length<2){
      document.querySelectorAll('section.sec, .walk, .gcard, .qgroup, .qa').forEach(function(el){el.classList.remove('hidden');});
      hit.textContent=''; return;
    }
    var n=0;
    document.querySelectorAll('section.sec, .walk, .gcard, .qgroup, .qa').forEach(function(el){
      var hitHere=el.getAttribute('data-search') && el.getAttribute('data-search').toLowerCase().indexOf(term)>=0;
      var textHit=el.innerText.toLowerCase().indexOf(term)>=0;
      if(el.tagName==='DETAILS'){
        if(!textHit){el.classList.add('hidden');}
        else {el.classList.remove('hidden'); el.open=true; n++;}
        return;
      }
      if(!hitHere && !textHit){el.classList.add('hidden');}
      else {el.classList.remove('hidden'); n++;}
    });
    hit.textContent=n+' block'+(n===1?'':'s');
  }
  input.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,180);});
  input.addEventListener('keydown',function(e){if(e.key==='Escape'){input.value='';run();}});
  document.addEventListener('keydown',function(e){
    if(e.key==='/' && document.activeElement!==input){e.preventDefault();input.focus();}
  });
  var exp=document.getElementById('expand');
  if(exp) exp.addEventListener('click',function(){
    var open=this.dataset.open==='1';
    document.querySelectorAll('details.qa').forEach(function(d){d.open=!open;});
    this.dataset.open=open?'0':'1'; this.textContent=open?'Expand all answers':'Collapse all answers';
  });
  var tt=document.getElementById('totop');
  if(tt) tt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
})();
