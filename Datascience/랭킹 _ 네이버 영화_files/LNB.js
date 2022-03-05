/**
 * @fileOverview nhn.movie.LNB.js
 * @requires jindo
 * @author kn@nhn.com
 *
 * [!주의]
 * 이 파일은 개편아닌 페이지들에도 삽입되기 때문에 진도 v2.x, v1.5.x 에서 동작하도록 작성됐습니다.
 * - 진도 네임스페이스(jindo.) 사용
 * - 진도 v1.5.3 기준으로 스크립트 작성했지만... v1.4나 그 전 버전도 동작함
 * - 진도 컴포넌트는 양쪽 다 호환되서 문제없음
 */
(function (jindo) {

var htDefaultOptions = {
    sMenuScrollBoxId: 'scrollbar',
    sHeaderId: 'header',
    nMinWidthForHorizontalMiddle: 1280
};
var oNavigator = jindo.$Agent().navigator();
nhn.movie.LNB = jindo.$Class({

    $init: function (htOptions) {
        this.option(htDefaultOptions);
        this.option(htOptions || {});
        this._oDocument = jindo.$Document();

        this._welMenuScrollBox = jindo.$Element(this.option('sMenuScrollBoxId'));
    	try{
    		// IE 7 및 IE8,9의 호환성 보기 모드에서 LNB고정 기능을 쓸 수 없고 스크롤을 넣어도 오류가 발생함
    		// 플래시,동영상 영역과 LNB가 겹치는 해상도에서는 적용하지 않음
    		if (!oNavigator.ie || (oNavigator.ie && oNavigator.version > 7 && this._oDocument.clientSize().width > 1095) ) {
	    		this._oMenuScrollBox = new jindo.ScrollBox(this._welMenuScrollBox.$value(), {
	    			nDelta: 32,
	    			sOverflowX: 'hidden',
	    			sOverflowY: 'auto'
	    		});
    		} else {
        		jindo.$Element(this.option('sHeaderId')).css('position', 'absolute');
    		}
    	}
    	catch(e){
    		this._oMenuScrollBox = undefined;
    	}

        this._nMenuWidth = this._welMenuScrollBox.$value().offsetWidth;
        this._nMenuOffsetTop = 47;

        this._wfWindowResize = jindo.$Fn(this._onWindowResize, this);
        this._wfWindowScroll = jindo.$Fn(this._onWindowScroll, this);

        this.update();
        this._wfWindowResize.attach(window, 'resize');
        this._wfWindowScroll.attach(window, 'scroll');
    },

    _onWindowResize: function (we) {
        this.update();
    },

    _onWindowScroll: function (we) {
        clearTimeout(this._nTimer);
        this._nTimer = null;
        this._nTimer = setTimeout(jindo.$Fn(function () {
        }, this).bind(), 0);
    },

    update: function () {
		// 스크롤박스 사이즈 조절
		// 상단 스크립트에서 _oMenuScrollBox 를 정의하는 부분에 오류가 있을 경우, 해당 로직을 실행하지 않음.
		if(this._oMenuScrollBox != undefined){
			var htDocSize = this._oDocument.clientSize();
    		this._nPrevMenuScrollTop = this._oMenuScrollBox.getScrollTop();
    		this._oMenuScrollBox.setSize(
    				this._nMenuWidth,
    				htDocSize.height - this._nMenuOffsetTop
    		);
    		this._oMenuScrollBox.setScrollTop(this._nPrevMenuScrollTop);
		} else {
			//IE7에서 LNB영역이 길게 안 늘어나는 문제가 있어 강제로 늘림
    		jindo.$Element(this.option('sHeaderId')).css('bottom', '0');
		}
    }

}).extend(jindo.Component);

})(jindo);