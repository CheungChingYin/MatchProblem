function set_cookie(e,t,n,o){var i,r,c=new Date;c.setTime(c.getTime()+24*(t||30)*60*60*1e3),i="; expires="+c.toGMTString();for(r in e)document.cookie=r+"="+e[r]+i+"; domain="+(n||"douban.com")+"; path="+(o||"/")}function get_cookie(e){var t,n,o=e+"=",i=document.cookie.split(";");for(t=0;t<i.length;t++){for(n=i[t];" "==n.charAt(0);)n=n.substring(1,n.length);if(0===n.indexOf(o))return n.substring(o.length,n.length).replace(/\"/g,"")}return null}