(function(g){var window=this;'use strict';var j4=function(a){g.U.call(this,{G:"div",L:"ytp-miniplayer-ui"});this.ye=!1;this.player=a;this.T(a,"minimized",this.jg);this.T(a,"onStateChange",this.bI)},k4=function(a){g.BL.call(this,a);
this.j=new j4(this.player);this.j.hide();g.oL(this.player,this.j.element,4);a.Te()&&(this.load(),g.L(a.getRootNode(),"ytp-player-minimized",!0))};
g.v(j4,g.U);g.h=j4.prototype;
g.h.NF=function(){this.tooltip=new g.yP(this.player,this);g.I(this,this.tooltip);g.oL(this.player,this.tooltip.element,4);this.tooltip.scale=.6;this.yc=new g.wM(this.player);g.I(this,this.yc);this.Mg=new g.U({G:"div",L:"ytp-miniplayer-scrim"});g.I(this,this.Mg);this.Mg.Ba(this.element);this.T(this.Mg.element,"click",this.nB);var a=new g.U({G:"button",Ha:["ytp-miniplayer-close-button","ytp-button"],W:{"aria-label":"\ub2eb\uae30"},V:[g.EI()]});g.I(this,a);a.Ba(this.Mg.element);this.T(a.element,"click",
this.Qi);a=new g.y_(this.player,this);g.I(this,a);a.Ba(this.Mg.element);this.eq=new g.U({G:"div",L:"ytp-miniplayer-controls"});g.I(this,this.eq);this.eq.Ba(this.Mg.element);this.T(this.eq.element,"click",this.nB);var b=new g.U({G:"div",L:"ytp-miniplayer-button-container"});g.I(this,b);b.Ba(this.eq.element);a=new g.U({G:"div",L:"ytp-miniplayer-play-button-container"});g.I(this,a);a.Ba(this.eq.element);var c=new g.U({G:"div",L:"ytp-miniplayer-button-container"});g.I(this,c);c.Ba(this.eq.element);this.ZO=
new g.XN(this.player,this,!1);g.I(this,this.ZO);this.ZO.Ba(b.element);b=new g.VN(this.player,this);g.I(this,b);b.Ba(a.element);this.nextButton=new g.XN(this.player,this,!0);g.I(this,this.nextButton);this.nextButton.Ba(c.element);this.Pg=new g.kP(this.player,this);g.I(this,this.Pg);this.Pg.Ba(this.Mg.element);this.Ic=new g.gO(this.player,this);g.I(this,this.Ic);g.oL(this.player,this.Ic.element,4);this.cB=new g.U({G:"div",L:"ytp-miniplayer-buttons"});g.I(this,this.cB);g.oL(this.player,this.cB.element,
4);a=new g.U({G:"button",Ha:["ytp-miniplayer-close-button","ytp-button"],W:{"aria-label":"\ub2eb\uae30"},V:[g.EI()]});g.I(this,a);a.Ba(this.cB.element);this.T(a.element,"click",this.Qi);a=new g.U({G:"button",Ha:["ytp-miniplayer-replay-button","ytp-button"],W:{"aria-label":"\ub2eb\uae30"},V:[g.KI()]});g.I(this,a);a.Ba(this.cB.element);this.T(a.element,"click",this.aY);this.T(this.player,"presentingplayerstatechange",this.Tc);this.T(this.player,"appresize",this.yb);this.T(this.player,"fullscreentoggled",
this.yb);this.yb()};
g.h.show=function(){this.Xd=new g.zp(this.Nq,null,this);this.Xd.start();this.ye||(this.NF(),this.ye=!0);0!==this.player.getPlayerState()&&g.U.prototype.show.call(this);this.Ic.show();this.player.unloadModule("annotations_module")};
g.h.hide=function(){this.Xd&&(this.Xd.dispose(),this.Xd=void 0);g.U.prototype.hide.call(this);this.player.Te()||(this.ye&&this.Ic.hide(),this.player.loadModule("annotations_module"))};
g.h.ra=function(){this.Xd&&(this.Xd.dispose(),this.Xd=void 0);g.U.prototype.ra.call(this)};
g.h.Qi=function(){this.player.stopVideo();this.player.Qa("onCloseMiniplayer")};
g.h.aY=function(){this.player.playVideo()};
g.h.nB=function(a){if(a.target===this.Mg.element||a.target===this.eq.element)this.player.U().S("kevlar_miniplayer_play_pause_on_scrim")?g.HH(this.player.zb())?this.player.pauseVideo():this.player.playVideo():this.player.Qa("onExpandMiniplayer")};
g.h.jg=function(){g.L(this.player.getRootNode(),"ytp-player-minimized",this.player.Te())};
g.h.Fd=function(){this.Ic.Qb();this.Pg.Qb()};
g.h.Nq=function(){this.Fd();this.Xd&&this.Xd.start()};
g.h.Tc=function(a){g.T(a.state,32)&&this.tooltip.hide()};
g.h.yb=function(){g.wO(this.Ic,0,this.player.gb().getPlayerSize().width,!1);g.jO(this.Ic)};
g.h.bI=function(a){this.player.Te()&&(0===a?this.hide():this.show())};
g.h.pc=function(){return this.tooltip};
g.h.Ze=function(){return!1};
g.h.Df=function(){return!1};
g.h.Ki=function(){return!1};
g.h.Zx=function(){};
g.h.Qn=function(){};
g.h.Vs=function(){};
g.h.zo=function(){return null};
g.h.Gw=function(){return null};
g.h.Hj=function(){return new g.Pm(0,0,0,0)};
g.h.handleGlobalKeyDown=function(){return!1};
g.h.handleGlobalKeyUp=function(){return!1};
g.h.Uq=function(a,b,c,d,e){var f=0,k=d=0,l=g.en(a);if(b){c=g.Hp(b,"ytp-prev-button")||g.Hp(b,"ytp-next-button");var m=g.Hp(b,"ytp-play-button"),n=g.Hp(b,"ytp-miniplayer-expand-watch-page-button");c?f=k=12:m?(b=g.cn(b,this.element),k=b.x,f=b.y-12):n&&(k=g.Hp(b,"ytp-miniplayer-button-top-left"),f=g.cn(b,this.element),b=g.en(b),k?(k=8,f=f.y+40):(k=f.x-l.width+b.width,f=f.y-20))}else k=c-l.width/2,d=25+(e||0);b=this.player.gb().getPlayerSize().width;e=f+(e||0);l=g.zh(k,0,b-l.width);e?(a.style.top=e+"px",
a.style.bottom=""):(a.style.top="",a.style.bottom=d+"px");a.style.left=l+"px"};
g.h.showControls=function(){};
g.h.Fl=function(){};
g.h.Vk=function(){return!1};g.v(k4,g.BL);k4.prototype.create=function(){};
k4.prototype.Zh=function(){return!1};
k4.prototype.load=function(){this.player.hideControls();this.j.show()};
k4.prototype.unload=function(){this.player.showControls();this.j.hide()};g.AL("miniplayer",k4);})(_yt_player);
