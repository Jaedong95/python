var searchDefaultImage = function(source, type){
    var sDefaultImage = "";
    switch(type){
        case 0:
            sDefaultImage = "https://ssl.pstatic.net/static/movie/2012/06/dft_img30x43.png";
            break;
        case 1:
            sDefaultImage = "https://ssl.pstatic.net/static/movie/2012/06/dft_img30x48.png";
            break;
    };
    source.src = sDefaultImage;
};

(function (jindo) {
var options = null;
var elAuto = null;
var bDirectClick = false;
var bOpenAuto = false;
var oFlag = {
    bMovie : false,
    bPeople : false
}

var template = {
    "area" : '<div id="jAutoComplate" class="auto_tx_area">'
                + '<div class="auto_tx_foorer">'
                + '<a href="#" class="all_result">전체 검색 결과보기</a>'
                + '<p class="auto_tx_etc">'
                + '<a href="http://help.naver.com/ops/step1/faq.nhn" target="_blank" class="helper">도움말</a>'
                + '<a href="#" class="clse">기능끄기</a>'
                + '</p>'
                + '<img src="https://ssl.pstatic.net/sstatic/search/images11/img_atcmp15.gif" alt="" width="218" height="23" class="help" id="help_tooltip2" style="position:absolute;bottom: 37px; right: 1px; display: none; ">'
                + '</div>'
                + '</div>',
    "auto_mv" : '<div id="jAutoMV" class="auto_mv">'
                + '<strong class="h_auto_mv">영화</strong>'
                + '<ul>'
                + '</ul>'
                + '</div>',
    "auto_mv_contents" : '<li data-title="{{title}}">'
                + '<a href="{{link}}">'
                + '<p class="auto_thumb"><img src="{{thumbnail}}" width="30" height="43" alt="{{title}}" onerror="searchDefaultImage(this,0);"/></p>'
                + '<div class="thumb_spec">'
                + '<p class="auto_tx_tit">{{title_match}} <span class="auto_since">{{time}}</span></p>'
                + '<p class="etc_spec">{{people}}</p>'
                + '</div>'
                + '</a><!-- N=a:GNB.sug -->'
                + '</li>',
    "auto_people" : '<div id="jAutoPP" class="auto_people">'
                + '<strong class="h_auto_people">영화인</strong>'
                + '<ul>'
                + '</ul>'
                + '</div>',
    "auto_people_contents" : '<li data-title="{{title}}">'
                + '<a href="{{link}}">'
                + '<p class="auto_thumb"><img src="{{thumbnail}}" width="30" height="38" alt="{{title}}" onerror="searchDefaultImage(this,1);"/></p>'
                + '<div class="thumb_spec">'
                + '<p class="auto_tx_tit">{{title_match}} <span class="auto_since">{{time}}</span></p>'
                + '<dl>'
                //+ '<dt>영화배우</dt>'
                + '{{movie}}'
                + '</dl>'
                + '</div>'
                + '</a><!-- N=a:GNB.sug -->'
                + '</li>'
};

nhn.movie.Search = jindo.$Class({
    options : {},
    $init: function (oOptions) {
        var _self = this;
        this.options = oOptions;
        options = this.options;
        var elArea = jindo.$Element(options.area);
        var bAutoClose = true;

        this._oCookie = jindo.$Cookie();
        this._auto = this._oCookie.get('NM_AUTOCOMPLETE') || "ON";

        try{
            jindo.$Element("jSearchArea").remove("jAutoComplate");
            elAuto = null;
            oFlag = {
                bMovie : false,
                bPeople : false
            };
            jindo.$Element('ipt_tx_srch').$value().value="";
        }catch(e){}

        // 검색영역 보여주기
        if( elArea ){
            var closeSearch = function(event){
                var parent = jindo.$Element(event.element).parent(function(v){
                    return v.hasClass("_view");
                });
                // 클릭했을 경우 위치가 외부 일 경우 닫힘(내부인 경우 닫히지 않음)
                if( parent.length > 0 ) return;
                // 포커스가 되지 않은 경우에 마우스가 빠져나가면 닫힘.
                if(event.type == "mousemove" && bAutoClose == false ) return;
//              jindo.$Element(elArea.query("._hide")).show();
//              jindo.$Element(elArea.query("._view")).hide();
//              try{
//                  jindo.$Element("jSearchArea").remove("jAutoComplate");
//                  elAuto = null;
//                  oFlag = {
//                      bMovie : false,
//                      bPeople : false
//                  };
//              }catch(e){}
//              jindo.$Element('ipt_tx_srch').$value().value="";

                if( bDirectClick ){
                    bDirectClick = false;
                    return;
                }
                try{
                    jindo.$Element("jAutoComplate").hide();
                }catch(e){}

                if( jindo.$Element('ipt_tx_srch').$value().value == ""){
                    jindo.$Element(jindo.$Element("jSearchArea").query(".ipt_srch label")).show();
                }

                if( elArea.query(".auto_tx img") ){
                    if( _self._auto == "ON" ){
                        _self.autoBtn("hide");
                    }
//                  jindo.$Element(elArea.query(".auto_tx img")).attr("src", "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_down.gif");
                }
                bAutoClose = true;

                jindo.$Fn(closeSearch,this).detach(document,"mousedown");
//              jindo.$Fn(closeSearch,this).detach(document,"mousemove");
            };
//
            jindo.$Fn(function(event){
                // 검색영역이 닫히는 경우 등록
                jindo.$Fn(closeSearch,this).attach(document,"mousedown"); //.attach(document,"mousemove");
                var parent = jindo.$Element(event.element).parent(function(v){
                    return v.hasClass("auto_tx_area");
                });
                // 클릭했을 경우 위치가 auto view 영역이면 멈춤
                if( parent.length > 0 ){
                    bDirectClick = true;
                    return;
                }
//              jindo.$Element(elArea.query("._hide")).hide();
//              jindo.$Element(elArea.query("._view")).show();
//              jindo.$Element('ipt_tx_srch').$value().focus();
            },this).attach(elArea,"mousedown");
//
            jindo.$Fn(function(event){
                // 입력 영역이 포커스 되었을 경우 닫히지 않음.
                try{
                    if( _self._auto == "ON" ){
                        if( jindo.$Element('ipt_tx_srch').$value().value != "" ){
                            if( bOpenAuto && jindo.$Element("jAutoComplate") && jindo.$Element("jAutoComplate").css("display") == "none"){
                                bOpenAuto = false;
                            }else if( !bOpenAuto && jindo.$Element("jAutoComplate") && jindo.$Element("jAutoComplate").css("display") != "none") {
                                bOpenAuto = true;
                            }
                            if( bOpenAuto == false ){
                                _self.autoBtn("show");
                                jindo.$Element("jAutoComplate").show();
                                bOpenAuto = true;
                            }else{
                                _self.autoBtn("hide");
                                jindo.$Element("jAutoComplate").hide();
                                bOpenAuto = false;
                            }
                        }
                    }
                }catch(e){}
                bDirectClick = false;
                jindo.$Element(jindo.$Element("jSearchArea").query(".ipt_srch label")).hide();
            },this).attach(jindo.$('ipt_tx_srch'),"click");

            // 검색 버튼을 누른 경우
            jindo.$Fn(function(event){
                if( jindo.$Element('ipt_tx_srch').$value().value.length <= 0 ) return;
                var elSearchForm = jindo.$Form("jSearchForm");
                if( elSearchForm ){
                    elSearchForm.value("query", (sTemp!="")?sTemp:jindo.$Element('ipt_tx_srch').$value().value);
                    elSearchForm.submit();
                }
            },this).attach(jindo.$Element(elArea.query(".btn_srch")),"click");

            jindo.$Fn(function(event){
                // 자동 완성 펼쳐보기
                if( _self._auto == "ON" ){

                    if( elAuto == null ){
                        _self.autoBtn("show");
                        makeAuto(null);
                    }else{
                        if( elAuto.css("display") != "none" ){
                            elAuto.hide();
                            _self.autoBtn("hide");
                        }else{
                            _self.autoBtn("show");
                            elAuto.show();
                            if( jindo.$Element('ipt_tx_srch').$value().value != "" ){
                                oWatchInput.fireChangeEvent();
                            }
                        }
                    }


                }else{
                    //자동 완성 키기
//                  jindo.$Element(elArea.query(".auto_tx img")).attr("src", "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_down.gif");
                    _self._setCookie('NM_AUTOCOMPLETE', 'ON');
                    _self._auto = "ON";
                    if( elAuto == null ){
                        makeAuto(null);
                    }else{
                        elAuto.show();
                    }
                    if( jindo.$Element('ipt_tx_srch').$value().value != "" ){
                        oWatchInput.fireChangeEvent();
                    }

                }
            },this).attach(jindo.$(elArea.query(".auto_tx")),"click");

        }

        // 자동완성
        var oWatchInput = new jindo.WatchInput(jindo.$('ipt_tx_srch'));
        elAuto = null;
        var bSelecting = false;
        var _self = this;
        var makeAuto = function(response){
            try{
                elArea.remove(jindo.$Element(elArea.query(".auto_tx_area")));
            }catch(e){}
            jindo.$Element(elArea.query(".btn_srch")).before(jindo.$(_self.makeTemplate()));
            setTimeout(function(){
                try{
                    _self.autoBtn("show");
//                  jindo.$Element(elArea.query(".auto_tx img")).attr("src", "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_up.gif");
                }catch(e){
                }
                elAuto =  jindo.$Element("jAutoComplate");
                try{
                    elAuto.show();
                    jindo.$Fn(function(event){
                        //전체 검색 결과 보기
                        var elSearchForm = jindo.$Form("jSearchForm");
                        if( elSearchForm ){
                            elSearchForm.value("query", (sTemp!="")?sTemp:jindo.$Element('ipt_tx_srch').$value().value);
                            elSearchForm.submit();
                        }
                    },this).attach(jindo.$(elAuto.query(".all_result")),"click");

                    jindo.$Fn(function(event){
                        //자동 완성 툴팁
                        try{
                            jindo.$Element(jindo.$Element("jAutoComplate").query("#help_tooltip2")).show();
                        }catch(e){}
                    },this).attach(jindo.$(elAuto.query(".clse")),"mouseover");
                    jindo.$Fn(function(event){
                        //자동 완성 툴팁
                        try{
                            jindo.$Element(jindo.$Element("jAutoComplate").query("#help_tooltip2")).hide();
                        }catch(e){}
                    },this).attach(jindo.$(elAuto.query(".clse")),"mouseout");

                    if( _self._auto == "ON" ){
                        jindo.$Fn(function(event){
                            //자동 완성 끄기
                            _self._setCookie('NM_AUTOCOMPLETE', 'OFF');
                            _self._auto = "OFF";
                            try{
                                _self.autoBtn("off");
//                              jindo.$Element(elArea.query(".auto_tx img")).attr("src", "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_down2.gif");
                                elArea.remove("jAutoComplate");
                                elAuto = null;
                                oFlag = {
                                    bMovie : false,
                                    bPeople : false
                                };
                                //jindo.$Element('ipt_tx_srch').$value().value="";
                            }catch(e){
                            }
                        },this).attach(jindo.$(elAuto.query(".clse")),"click");
                    }else{
                        jindo.$Fn(function(event){
                            //자동 완성 키기
                            _self._setCookie('NM_AUTOCOMPLETE', 'ON');
                            _self._auto = "ON";
                        },this).attach(jindo.$(elAuto.query(".clse")),"click");
                    }
                    if( response != null ){
                        try{
                            jindo.$Element("jAutoComplate").remove("jInfomation");
                        }catch(e){}
                        _self.makeContents(response, oFlag);
                    }else{
                        jindo.$Element("jAutoComplate").prepend(jindo.$('<p id="jInfomation" class="at_alert">자동완성 기능이 활성화되었습니다.</p>'));
                    }
                }catch(e){

                }
            },0);
        }
        oWatchInput.attach('change', function(oCustomEvent){
            if( _self._auto != "ON" ) return;
            if( bSelecting ) return;
            var query = oCustomEvent.sText.replace(/\#/g,"%23");
            if( query.length > 0 ){
                //jindo.$Element("jSearchArea").query(".ipt_srch label").hide();
                var oAjax = new jindo.$Ajax(options.autosearch + encodeURI(query), {
                    type: 'jsonp',
                    onload: function(res){
                        var response = res.json();
                            if( elAuto == null ){
                                makeAuto(response);
                            }else{
                                _self.makeContents(response, oFlag);
                            }
                    }
                });
                oAjax.request();

            }else{
                // 자동 완성 영역을 삭제 한다.
                if( elArea && jindo.$("jAutoComplate") ){
                    try{
                        elArea.remove("jAutoComplate");
                        _self.autoBtn("hide");
//                      jindo.$Element(elArea.query(".auto_tx img")).attr("src", "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_down.gif");
                        jindo.$Element('ipt_tx_srch').$value().value="";
                        //jindo.$Element("jSearchArea").query(".ipt_srch label").show();
                    }catch(e){}
                }
                elAuto = null;
                oFlag = {
                    bMovie : false,
                    bPeople : false
                }
            }
        });

        // 키보드 입력
        var aSelectingList = [];
        var iIndex = 0;
        var sTemp = "";
        var elTempBefore = null;
        jindo.$Fn(function(event){
            switch(event._event.keyCode){
                case 38:
                    bSelecting = true;
                    if( iIndex > 0 ) iIndex--;
                    break;
                case 40:
                    if( bSelecting && iIndex < aSelectingList.length ) iIndex++;
                    bSelecting = true;
                    break;
                case 13:
                    if( bSelecting ){
                        event.stop(jindo.$Event.CANCEL_ALL);
                        document.location.href = jindo.$Element(jindo.$Element(aSelectingList[iIndex]).query("a")).attr("href");
                    }else{
                        var elSearchForm = jindo.$Form("jSearchForm");
                        if( elSearchForm ){
                            elSearchForm.value("query", jindo.$Element('ipt_tx_srch').$value().value);
                            elSearchForm.submit();
                        }
                        event.stopDefault();
                    }
                    break;
                default:
                    bSelecting = false;
                    break;
            }

            if( bSelecting ){
                if(aSelectingList.length == 0 ){
                    aSelectingList = elArea.queryAll("li");
                    sTemp = jindo.$Element(event.element).$value().value;
                }

                if( elTempBefore != null ){
                    jindo.$Element(elTempBefore.query("a")).removeClass("m_over");
                    jindo.$Element(elTempBefore.query("a")).removeClass("p_over");
                }

                if( iIndex == aSelectingList.length ){
                    iIndex = 0;
                    jindo.$Element(event.element).$value().value = sTemp;
                    setTimeout(function(){
                        bSelecting = false;
                    },600);
                    elTempBefore = null;
                } else {
                    jindo.$Element(event.element).$value().value = jindo.$Element(aSelectingList[iIndex]).attr("data-title");
                    jindo.$Element(jindo.$Element(aSelectingList[iIndex]).query("a")).addClass("m_over");
                    elTempBefore = jindo.$Element(aSelectingList[iIndex]);
                }
            }else{
                aSelectingList = [];
                iIndex = 0;
                sTemp = "";
            }


        },this).attach(jindo.$('ipt_tx_srch'), "keydown");

    },
    makeAutoText : function(query, value){
        var sTempValue = value.replace(/\s/g, "");
        var sQuery = new RegExp("("+jindo.$S(query).escapeRegex()+")+","gi");
        var aMatch = sTempValue.match(sQuery);
        if( aMatch != null ){
            // 무엇인가 매치가 되는 것이 있다.
            // space 여부 확인
            var tempMatch = value.match(/\s/g);
            var iEIndex = 0;
            var iSIndex = 0;
            var iLastIndex = value.lastIndexOf(" ");
            var iLength = value.length;
            var iSpaceCount = 0;
            var rSpacePosition = [];
            var sTempValueMatch = "";

            if( tempMatch != null ){
                for( var i = 0 ; i <= tempMatch.length; i++ ){
                    if( iEIndex == iLastIndex){
                        iEIndex = iLength;
                    }else{
                        iEIndex = value.indexOf(" ",iSIndex);
                    }
                    iSpaceCount++;
                    rSpacePosition.push(iEIndex);
                    iSIndex = iEIndex + 1;
                }
                sTempResult = "";//sTempValue.replace(sQuery,"<em>$1</em>");
                jindo.$A(aMatch).forEach(function(v,i,a){
                    if( i == 0 ){
                        sTempResult = sTempValue.replace(v,"<em>"+v+"</em>");
                    }
                });

                var sFinalResult = "";
                if(iSIndex > 0 ){
                    var iTempStart = 0;
                    var iSpacePositionLen = rSpacePosition.length;
                    var iPlusTag = 0;
                    var iOldV = 0;

                    jindo.$A(rSpacePosition).forEach(function(v,i,a){

                        var iFindTag = sTempResult.indexOf("<",iTempStart);
                        var iTagEnd = (v+iPlusTag-i);

                        if( iFindTag >= 0 && iFindTag <= iTagEnd ){
                            iPlusTag += sTempResult.indexOf(">",iTempStart) - sTempResult.indexOf("<",iTempStart) + 1;
                            var iTempNextTag = sTempResult.indexOf("</",iTagEnd);
                            if( iTempNextTag > -1 && iTempNextTag < v+iPlusTag-i) {
                                // 태그 된 안에 스페이스가 없다.
                                var iCloseTagEnd = sTempResult.indexOf(">",iTempNextTag);
                                sFinalResult += sTempResult.slice(iTempStart,iCloseTagEnd+1);
                                iTempStart = iCloseTagEnd + 1;

                                if( iCloseTagEnd+1 ==  v+iPlusTag-i){
                                    // 바로 다음이 스페이스면
                                    sFinalResult += " ";
                                }else{
                                    iPlusTag += iCloseTagEnd - iTempNextTag + 1;

                                    //다음 스페이스를 찾는다.
                                    sFinalResult += sTempResult.slice(iTempStart, v+iPlusTag-i) + " ";
                                    iTempStart = v + iPlusTag - i;
                                }

                            }else{
                                sFinalResult += sTempResult.slice(iTempStart,v+iPlusTag-i) + " ";
                                iTempStart = v + iPlusTag - i;
                            }


                        }else{
                            sFinalResult += sTempResult.slice(iTempStart,v+iPlusTag-i) + " ";
                            iTempStart = v + iPlusTag - i;
                        }
                    });

                    return sFinalResult;
                }else{
                    //그냥 변경
                    return value.replace(sQuery,"<em>$1</em>");
                }
            }else{
                //그냥 변경
            	return value.replace(new RegExp("("+jindo.$S(query).escapeRegex()+")","i"),"<em>$1</em>");
            }
        }else{
        	return value;
        }
    },
    makeLists : function(value, query){
        var self = this;
        var sHTML = "";

        switch(value[6][0]){
            case "movie":
                sHTML = template.auto_mv_contents
                        .replace(/{{title}}/g, value[0][0])
                        .replace("{{title_match}}",self.makeAutoText(query, value[0][0]))
                        .replace("{{time}}", value[1][0].slice(0,4))
                        .replace("{{people}}", value[2][0])
                        .replace("{{thumbnail}}", (value[3][0])?value[3][0].replace("http://movie.phinf.naver.net", "https://movie-phinf.pstatic.net")+"?type=n30_43_2":"https://ssl.pstatic.net/static/movie/2012/06/dft_img30x43.png")
                        .replace("{{link}}", options.movelink + value[5][0]);
                break;
            case 'people':
                var escapedImageSrc = encodeURIComponent(value[3][0]);
                sHTML = template.auto_people_contents
                        .replace(/{{title}}/g, value[0][0])
                        .replace("{{title_match}}",self.makeAutoText(query, value[0][0]))
                        .replace("{{time}}", (value[1][0] != 0 )?value[1][0]:"")
                        .replace("{{movie}}", (value[2][0])?"<dd>"+ value[2][0] +"</dd>": "")
                        .replace("{{thumbnail}}", (value[3][0])?"https://search.pstatic.net/common/?src=" + escapedImageSrc + "&type=o120_150&quality=95" :"https://ssl.pstatic.net/static/movie/2012/06/dft_img30x48.png")
                        .replace("{{link}}", options.peoplelink + value[5][0]);
                break;
        }
        return sHTML;
    },
    makeContents : function(aItems, oFlag){
        var bPeople = false;
        var bMoive = false;
        var _self = this;
        elAuto = jindo.$Element("jAutoComplate");
        try{
            jindo.$Element("jAutoComplate").remove("jInfomation");
        }catch(e){};
        try{
            jindo.$Element(jindo.$Element("jAutoPP").query("ul")).html("");
        }catch(e){};
        try{
            jindo.$Element(jindo.$Element("jAutoMV").query("ul")).html("");
        }catch(e){};

        if( aItems.items.length > 0 ) {

            if( aItems.items[0].length > 0 ){
                try{
                    jindo.$Element("jAutoComplate").show();
                    elAuto.show();
                }catch(e){}
            }

            jindo.$A(aItems.items[0]).forEach(function(v,i,a){
                if( typeof v[6] == "undefined" ) {
                    return;
                }
                switch(v[6][0]){
                    case "movie":
                        bMoive = true;
                        if( !oFlag.bMovie ){
                            if( oFlag.bPeople ){
                                try{
                                    jindo.$Element("jAutoPP").before(jindo.$(template.auto_mv));
                                }catch(e){}
                            }else{
                                try{
                                    elAuto.prepend(jindo.$(template.auto_mv));
                                }catch(e){}
                            }
                            oFlag.bMovie = true;
                            try{
                                jindo.$Element(jindo.$Element("jAutoMV").query("ul")).html(_self.makeLists(v, aItems.query[0]));
                            }catch(e){}
                        }else{
                            try{
                                jindo.$Element(jindo.$Element("jAutoMV").query("ul")).append(jindo.$(_self.makeLists(v, aItems.query[0])));
                            }catch(e){}
                        }
                        break;
                    case "people":
                        // 인물
                        bPeople = true;
                        if( !oFlag.bPeople ){
                            if( oFlag.bMovie ){
                                try{
                                    jindo.$Element("jAutoMV").after(jindo.$(template.auto_people));
                                }catch(e){}

                            }else{
                                try{
                                    elAuto.prepend(jindo.$(template.auto_people));
                                }catch(e){}
                            }
                            oFlag.bPeople = true;
                            try{
                                jindo.$Element(jindo.$Element("jAutoPP").query("ul")).html(_self.makeLists(v, aItems.query[0]));
                            }catch(e){}
                        }else{
                            try{
                                jindo.$Element(jindo.$Element("jAutoPP").query("ul")).append(jindo.$(_self.makeLists(v, aItems.query[0])));
                            }catch(e){}
                        }
                        break;
                }
            });
            // 정리
            if( !bPeople ){
                try{
                    elAuto.remove("jAutoPP");
                }catch(e){}
                oFlag.bPeople = false;
            }
            if( !bMoive ){
                try{
                    elAuto.remove("jAutoMV");
                }catch(e){}
                oFlag.bMovie = false;
            }
            if( !bPeople && !bMoive ){
                //데이터가 없지만, 어레이가 있는 경우가 있음
                try{
                    elAuto.hide();
                }catch(e){}

            }else{
                try{
                    elAuto.show();
                }catch(e){}
            }

        }else{
            // 자동완성 할 것이 없는 경우
            jindo.$Element(options.area).remove(jindo.$Element("jAutoComplate"));
            elAuto = null;
            oFlag = {
                bMovie : false,
                bPeople : false
            };
        }



    },
    makeTemplate : function(){
        return template.area;
    },
    autoBtn : function(sStat){
        var options = this.options;
        var img = "";
        var title = "";
        switch(sStat){
            case "show":
                img = "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_up.gif";
                title = "자동완성 접기";
                break;
            case "hide":
                img = "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_down.gif";
                title = "자동완성 펼치기";
                break;
            case "off":
                img = "https://ssl.pstatic.net/static/movie/2012/06/srch_arrow_down2.gif";
                title = "자동완성 켜기";
                break;
        }
        jindo.$Element(jindo.$Element(options.area).query(".auto_tx img")).attr("src", img).attr("title", title).attr("alt", title);
        jindo.$Element(jindo.$Element(options.area).query(".auto_tx a")).attr("title", title);
    },
    _setCookie: function (sName, sValue) {
        document.cookie = sName + '=' + sValue + '; path=/; domain=.movie.naver.com';
    }

}).extend(jindo.Component);

})(jindo);