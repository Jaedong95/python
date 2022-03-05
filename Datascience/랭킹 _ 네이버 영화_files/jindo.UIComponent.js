/**
 * Jindo Component
 * @version 1.0.2
 * NHN_Library:Jindo_Component-1.0.2;JavaScript Components for Jindo;
 */


jindo.UIComponent=jindo.$Class({$init:function(){this._bIsActivating=false;},isActivating:function(){return this._bIsActivating;},activate:function(){if(this.isActivating()){return this;}
this._bIsActivating=true;if(arguments.length>0){this._onActivate.apply(this,arguments);}else{this._onActivate();}
return this;},deactivate:function(){if(!this.isActivating()){return this;}
this._bIsActivating=false;if(arguments.length>0){this._onDeactivate.apply(this,arguments);}else{this._onDeactivate();}
return this;}}).extend(jindo.Component);