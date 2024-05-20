from bs4 import BeautifulSoup

html ="""
<!DOCTYPE html>

<html class="no-js" lang="en">
<head>
<!-- charset must appear in the first 1024 bytes of the document -->
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<title>Volume 151 Issue 7 | Development | The Company of Biologists</title>
<script class="cookiepro-otautoblock" src="https://cookie-cdn.cookiepro.com/consent/aa16308e-8418-4f98-934b-67ce9fe9c63b/OtAutoBlock.js" type="text/javascript"></script>
<script charset="UTF-8" class="cookiepro-otsdkstub" data-domain-script="aa16308e-8418-4f98-934b-67ce9fe9c63b" src="https://cookie-cdn.cookiepro.com/scripttemplates/otSDKStub.js" type="text/javascript"></script>
<script type="text/javascript">
        function OptanonWrapper() {
            // Get initial OnetrustActiveGroups ids
            if (typeof OptanonWrapperCount == "undefined") {
                otGetInitialGrps();
            }

            //Delete cookies
            otDeleteCookie(otIniGrps);

            // Assign OnetrustActiveGroups to custom variable
            function otGetInitialGrps() {
                OptanonWrapperCount = '';
                otIniGrps = OnetrustActiveGroups;
            }

            function otDeleteCookie(iniOptGrpId) {
                var otDomainGrps = JSON.parse(JSON.stringify(Optanon.GetDomainData().Groups));
                var otDeletedGrpIds = otGetInactiveId(iniOptGrpId, OnetrustActiveGroups);
                if (otDeletedGrpIds.length != 0 && otDomainGrps.length != 0) {
                    for (var i = 0; i < otDomainGrps.length; i++) {
                        //Check if CustomGroupId matches
                        if (otDomainGrps[i]['CustomGroupId'] != '' && otDeletedGrpIds.includes(otDomainGrps[i]['CustomGroupId'])) {
                            for (var j = 0; j < otDomainGrps[i]['Cookies'].length; j++) {
                                // console.log("otDeleteCookie",otDomainGrps[i]['Cookies'][j]['Name'])
                                //Delete cookie
                                eraseCookie(otDomainGrps[i]['Cookies'][j]['Name']);
                            }
                        }

                        //Check if Hostid matches
                        if (otDomainGrps[i]['Hosts'].length != 0) {
                            for (var j = 0; j < otDomainGrps[i]['Hosts'].length; j++) {
                                //Check if HostId presents in the deleted list and cookie array is not blank
                                if (otDeletedGrpIds.includes(otDomainGrps[i]['Hosts'][j]['HostId']) && otDomainGrps[i]['Hosts'][j]['Cookies'].length != 0) {
                                    for (var k = 0; k < otDomainGrps[i]['Hosts'][j]['Cookies'].length; k++) {
                                        //Delete cookie
                                        eraseCookie(otDomainGrps[i]['Hosts'][j]['Cookies'][k]['Name']);
                                    }
                                }
                            }
                        }

                    }
                }
                otGetInitialGrps(); //Reassign new group ids
            }

            //Get inactive ids
            function otGetInactiveId(customIniId, otActiveGrp) {
                //Initial OnetrustActiveGroups
                // console.log("otGetInactiveId",customIniId)
                customIniId = customIniId.split(",");
                customIniId = customIniId.filter(Boolean);

                //After action OnetrustActiveGroups
                otActiveGrp = otActiveGrp.split(",");
                otActiveGrp = otActiveGrp.filter(Boolean);

                var result = [];
                for (var i = 0; i < customIniId.length; i++) {
                    if (otActiveGrp.indexOf(customIniId[i]) <= -1) {
                        result.push(customIniId[i]);
                    }
                }
                return result;
            }

            //Delete cookie
            function eraseCookie(name) {
                //Delete root path cookies
                domainName = window.location.hostname;
                document.cookie = name + '=; Max-Age=-99999999; Path=/;Domain=' + domainName;
                document.cookie = name + '=; Max-Age=-99999999; Path=/;';

                //Delete LSO incase LSO being used, cna be commented out.
                localStorage.removeItem(name);

                //Check for the current path of the page
                pathArray = window.location.pathname.split('/');
                //Loop through path hierarchy and delete potential cookies at each path.
                for (var i = 0; i < pathArray.length; i++) {
                    if (pathArray[i]) {
                        //Build the path string from the Path Array e.g /site/login
                        var currentPath = pathArray.slice(0, i + 1).join('/');
                        document.cookie = name + '=; Max-Age=-99999999; Path=' + currentPath + ';Domain=' + domainName;
                        document.cookie = name + '=; Max-Age=-99999999; Path=' + currentPath + ';';
                        //Maybe path has a trailing slash!
                        document.cookie = name + '=; Max-Age=-99999999; Path=' + currentPath + '/;Domain=' + domainName;
                        document.cookie = name + '=; Max-Age=-99999999; Path=' + currentPath + '/;';


                    }
                }

            }
        }
    </script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js" type="text/javascript"></script>
<script>window.jQuery || document.write('<script src="//cob.silverchair-cdn.com/Themes/Silver/app/js/jquery.3.4.1.min.js" type="text/javascript">\x3C/script>')</script>
<script src="//cob.silverchair-cdn.com/Themes/Silver/app/vendor/v-638473440325722869/jquery-migrate-3.1.0.min.js" type="text/javascript"></script>
<script async="async" class="optanon-category-C0004" src="https://platform-api.sharethis.com/js/sharethis.js#property=643701de45aa460012e1032e&amp;product=sop" type="text/plain"></script>
<meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
<meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
<!-- Turn off telephone number detection. -->
<meta content="telephone=no" name="format-detection"/>
<!-- Bookmark Icons -->
<link href="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/apple-touch-icon808323293.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/favicon-32x32-1428583863.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/favicon-16x16-1159682937.png" rel="icon" sizes="16x16" type="image/png"/>
<link color="#5bbad5" href="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/safari-pinned-tab1999309873.svg" rel="mask-icon"/>
<link href="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/favicon662918389.ico" rel="icon"/>
<meta content="#002f65" name="theme-color"/>
<link href="//cob.silverchair-cdn.com/Themes/Client/app/css/v-638488182842692149/site.min.css" rel="stylesheet" type="text/css">
<link href="//cob.silverchair-cdn.com/Themes/Silver/app/icons/v-638473440312722733/style.css" rel="stylesheet" type="text/css">
<link href="//cob.silverchair-cdn.com/Themes/Client/app/css/v-638473439426493145/bg_img.css" rel="stylesheet" type="text/css">
<link href="https://use.typekit.net/jkq7xuh.css" rel="stylesheet"/>
<link href="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/CSS/dev/v-637530869184429003/site.css" rel="stylesheet" type="text/css">
<script>
                (function (w, d, s, l, i) {
                    w[l] = w[l] || []; w[l].push({
                        'gtm.start':
                            new Date().getTime(), event: 'gtm.js'
                    }); var f = d.getElementsByTagName(s)[0],
                        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
                        j.setAttribute('type', 'text/plain');
                        j.setAttribute('class', 'optanon-category-C0002');
                        j.async = true; j.src =
                        'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
                })(window, document, 'script', 'dataLayer', 'GTM-5KXMNBB');
            </script>
<script>
                (function (w, d, s, l, i) {
                    w[l] = w[l] || []; w[l].push({
                        'gtm.start':
                            new Date().getTime(), event: 'gtm.js'
                    }); var f = d.getElementsByTagName(s)[0],
                        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
                        j.setAttribute('type', 'text/plain');
                        j.setAttribute('class', 'optanon-category-C0002');
                        j.async = true; j.src =
                        'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
                })(window, document, 'script', 'dataLayer', 'GTM-T6TZKLZ');
            </script>
<script type="text/javascript">
            var App = App || {};
            App.LoginUserInfo = {
                isInstLoggedIn: 0,
                isIndividualLoggedIn: 0
            };

            App.CurrentSubdomain = 'dev';
            App.SiteURL = 'journals.biologists.com/dev';
        </script>
<meta content="Development | 151 | 7 | April 2024" name="description"/>
<link href="https://journals.biologists.com/dev/issue/151/7" rel="canonical">
<script type="application/ld+json">
        {"@context":"https://schema.org","@type":"PublicationIssue","@id":"https://journals.biologists.com/dev/issue/151/7","datePublished":"2024-04-01","issueNumber":"7","isPartOf":{"@id":"https://journals.biologists.com/dev","@type":"Periodical","volumeNumber":"151","name":"","publisher":{"@type":"Organization","name":"","logo":{"@type":"ImageObject","url":"//cob.silverchair-cdn.com/Themes/Client/app/img/favicons/favicon.ico"}},"issn":["1477-9129"]},"inLanguage":"en","copyrightHolder":"","copyrightYear":"2024","description":"","thumbnailURL":"https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/m_develop_151_7.cover.png?Expires=1777019121&Signature=VW2JF2pVK3cC3rcl4G98enrtfAl3efX7N4X1EfeLTnjRbB7fxjKYM7Ju75CQFfuI5q~~XPrX-148UZiuoVHLk1nKMmbWy7nD~-bEVUU0SD-~4R-xONQgOqkcw2UOJk8ctEQEbHf3t~cjiZsdYEH~WxGXsXrFcHXKSjKQceT8ylbj4bdy0xCQ5XOmbiJ8mZFtBpAMyHkkm6WQJBUiLQp0KUXzxdjREnt3VlMDnB4Gg2odmlYs1mqxsr2qZ3VU0TCkMTkLIwnr1V7CEhscXHL5bNs04dUVqQE64oCI78GJeur5FbwMi00hUkhwgjWaTYTSRLH7oOJufnMuSAAKty-qQg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA","image:alt":"Issue Cover"}
    </script>
<meta content="" property="og:site_name">
<meta content="" property="og:title">
<meta content="" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="" property="og:url"/>
<meta content="" property="og:updated_time"/>
<meta content="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/m_develop_151_7.cover.png?Expires=1777019121&amp;Signature=VW2JF2pVK3cC3rcl4G98enrtfAl3efX7N4X1EfeLTnjRbB7fxjKYM7Ju75CQFfuI5q~~XPrX-148UZiuoVHLk1nKMmbWy7nD~-bEVUU0SD-~4R-xONQgOqkcw2UOJk8ctEQEbHf3t~cjiZsdYEH~WxGXsXrFcHXKSjKQceT8ylbj4bdy0xCQ5XOmbiJ8mZFtBpAMyHkkm6WQJBUiLQp0KUXzxdjREnt3VlMDnB4Gg2odmlYs1mqxsr2qZ3VU0TCkMTkLIwnr1V7CEhscXHL5bNs04dUVqQE64oCI78GJeur5FbwMi00hUkhwgjWaTYTSRLH7oOJufnMuSAAKty-qQg__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" property="og:image"/>
<meta content="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/m_develop_151_7.cover.png?Expires=1777019121&amp;Signature=VW2JF2pVK3cC3rcl4G98enrtfAl3efX7N4X1EfeLTnjRbB7fxjKYM7Ju75CQFfuI5q~~XPrX-148UZiuoVHLk1nKMmbWy7nD~-bEVUU0SD-~4R-xONQgOqkcw2UOJk8ctEQEbHf3t~cjiZsdYEH~WxGXsXrFcHXKSjKQceT8ylbj4bdy0xCQ5XOmbiJ8mZFtBpAMyHkkm6WQJBUiLQp0KUXzxdjREnt3VlMDnB4Gg2odmlYs1mqxsr2qZ3VU0TCkMTkLIwnr1V7CEhscXHL5bNs04dUVqQE64oCI78GJeur5FbwMi00hUkhwgjWaTYTSRLH7oOJufnMuSAAKty-qQg__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" property="og:image:url"/>
<meta content="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/m_develop_151_7.cover.png?Expires=1777019121&amp;Signature=VW2JF2pVK3cC3rcl4G98enrtfAl3efX7N4X1EfeLTnjRbB7fxjKYM7Ju75CQFfuI5q~~XPrX-148UZiuoVHLk1nKMmbWy7nD~-bEVUU0SD-~4R-xONQgOqkcw2UOJk8ctEQEbHf3t~cjiZsdYEH~WxGXsXrFcHXKSjKQceT8ylbj4bdy0xCQ5XOmbiJ8mZFtBpAMyHkkm6WQJBUiLQp0KUXzxdjREnt3VlMDnB4Gg2odmlYs1mqxsr2qZ3VU0TCkMTkLIwnr1V7CEhscXHL5bNs04dUVqQE64oCI78GJeur5FbwMi00hUkhwgjWaTYTSRLH7oOJufnMuSAAKty-qQg__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" property="og:image:secure_url"/>
<meta content="Issue Cover" property="og:image:alt"/>
<script async="async" class="optanon-category-C0004" src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" type="text/plain"></script>
<script>
        var SCM = SCM || {};
        SCM.pubGradeAdsEnabled = false;
    </script>
<script>
    var googletag = googletag || {};
    googletag.cmd = googletag.cmd || [];

    googletag.cmd.push(function () {
    googletag.pubads().disableInitialLoad();


    });
</script>
<script src="https://js.stripe.com/v3/"></script>
</meta></meta></link></link></link></link></link></head>
<body class="off-canvas pg_Issue pg_issue" data-sitename="development" data-sitestyletemplate="Journal" theme-dev="">
<noscript>
<iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-5KXMNBB" style="display:none;visibility:hidden" width="0"></iframe>
</noscript>
<noscript>
<iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-T6TZKLZ" style="display:none;visibility:hidden" width="0"></iframe>
</noscript>
<a class="skipnav" href="#skipNav">Skip to Main Content</a>
<input id="hdnSiteID" name="hdnSiteID" type="hidden" value="1000005"/><input id="hdnAdDelaySeconds" name="hdnAdDelaySeconds" type="hidden" value="3000"/><input id="hdnAdConfigurationTop" name="hdnAdConfigurationTop" type="hidden" value="basic"/><input id="hdnAdConfigurationRightRail" name="hdnAdConfigurationRightRail" type="hidden" value="basic"/>
<section class="master-header row vt-site-header">
<div class="ad-banner js-ad-banner">
<div class="widget-AdBlock widget-instance-HeaderAd">
<input class="hfAdBlockInfo" data-accountid="" data-adprovider-typeid="1" data-divid="div-gpt-ad-1593437333707-0" data-enabled-on-mobile="True" data-outofpagead="False" data-sizes="[[728, 90]]" data-slotname="/155913954/DEV" data-sticky-time="5" data-targetname="" type="hidden"/>
<div class="adblock-wrap js-adblock-wrap" style="width:728px;">
<p class="adblock-advertisement-text js-adblock-advertisement-text hide">Advertisement</p>
<div adslot="/155913954/DEV" class="adblock-slot-placeholder js-adblock" id="div-gpt-ad-1593437333707-0" style="width:728px; height:90px;"></div>
</div>
</div>
</div>
<div class="widget-SitePageHeader widget-instance-SitePageHeader">
<div class="site-theme-header">
<div class="site-theme-header_contents global-nav-base">
<div class="global-nav">
<a class="js-dropdown-trigger global-nav-trigger" href="javascript:;">
<picture>
<source media="(min-width: 601px)" srcset="//cob.silverchair-cdn.com/UI/app/svg/umbrella/logo.svg"/>
<img alt="The Company of Biologists logo" class="logo-Development site-theme-header-image" src="//cob.silverchair-cdn.com/UI/app/svg/umbrella/logo.svg"/>
</picture>
<i class="icon-general_arrow-down arrow-icon"></i>
</a>
<nav class="navbar-menu global-nav-dropdown js-dropdown">
<div class="site-theme-header-logo">
<a class="site-theme-header-image-wrap" href="/">
<picture>
<source media="(min-width: 601px)" srcset="//cob.silverchair-cdn.com/UI/app/svg/umbrella/logo.svg"/>
<img alt="The Company of Biologists logo" class="logo-Development site-theme-header-image" src="//cob.silverchair-cdn.com/UI/app/svg/umbrella/logo.svg"/>
</picture>
</a>
<a class="icon-general-close menu-close js-menu-close" href="javascript:;"><span class="screenreader-text">Close</span></a>
</div>
<ul class="site-menu site-menu-lvl-0 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-0 site-menu-item-Journals" id="site-menu-item-8100">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">Journals <i class="icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1 site-menu-item-Development" id="site-menu-item-8102">
<a class="nav-link" href="/dev">Development </a>
</li>
<li class="site-menu-item site-menu-lvl-1 site-menu-item-Journal-of-Cell-Science" id="site-menu-item-8103">
<a class="nav-link" href="/jcs">Journal of Cell Science </a>
</li>
<li class="site-menu-item site-menu-lvl-1 site-menu-item-Journal-of-Experimental-Biology" id="site-menu-item-8104">
<a class="nav-link" href="/jeb">Journal of Experimental Biology </a>
</li>
<li class="site-menu-item site-menu-lvl-1 site-menu-item-Disease-Models-&amp;-Mechanisms" id="site-menu-item-8105">
<a class="nav-link" href="/dmm">Disease Models &amp; Mechanisms </a>
</li>
<li class="site-menu-item site-menu-lvl-1 site-menu-item-Biology-Open" id="site-menu-item-8106">
<a class="nav-link" href="/bio">Biology Open </a>
</li>
</ul>
</li>
<li class="site-menu-item site-menu-lvl-0 site-menu-item-Community-sites" id="site-menu-item-8101">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">Community sites <i class="icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1 site-menu-item-The-Node" id="site-menu-item-8107">
<a class="nav-link" href="https://thenode.biologists.com/">The Node </a>
</li>
<li class="site-menu-item site-menu-lvl-1 site-menu-item-preLights" id="site-menu-item-8108">
<a class="nav-link" href="https://prelights.biologists.com/">preLights </a>
</li>
<li class="site-menu-item site-menu-lvl-1 site-menu-item-FocalPlane" id="site-menu-item-8109">
<a class="nav-link" href="https://focalplane.biologists.com/">FocalPlane </a>
</li>
</ul>
</li>
<li class="site-menu-item site-menu-lvl-0 site-menu-item-For-librarians" id="site-menu-item-8110">
<a class="nav-link" href="https://www.biologists.com/library-hub/">For librarians </a>
</li>
</ul>
</nav>
</div>
<div class="mobile-menu-trigger_wrap mobile-search_wrap">
<a aria-expanded="false" class="mobile-search_toggle at-search-toggle" data-theme-dropdown-trigger="search-dropdown" href="javascript:;" role="button"><i class="icon-menu_search"><span class="screenreader-text">Search Dropdown Menu</span></i></a>
</div>
<div class="navbar-search-container mobile-dropdown search-dropdown" data-theme-dropdown="search-dropdown">
<div class="navbar-search">
<form class="microsite-search js-MicrositeSearch">
<fieldset class="searchbar-fieldset">
<legend><span class="screenreader-text">header search</span></legend>
<div class="navbar-search-input_wrap">
<label for="MicrositeSearchTerm-SitePageHeader"><span class="screenreader-text">search input</span></label>
<input autocomplete="off" class="navbar-search-input microsite-search-term at-microsite-search-term search-term-autosuggest" data-autosuggest-hint="micrositeSearchTermInputHint-SitePageHeader" data-autosuggest-id="MicrositeSearchTerm-SitePageHeader" data-autosuggest-results="micrositeAutoCompleteResults-SitePageHeader" data-searchfilter="search-filter-SitePageHeader" id="MicrositeSearchTerm-SitePageHeader" maxlength="255" placeholder="Search..." title="search input" type="text"/>
<input aria-hidden="true" class="hfAutoCompleteMaxResults" name="hfAutoCompleteMaxResults" type="hidden" value="6">
<input aria-hidden="true" class="hfSolrAutoSuggestMinimumCharactersLength" name="hfSolrAutoSuggestMinimumCharactersLength" type="hidden" value="2"/>
<input aria-hidden="true" class="hfSolrJournalName" name="hfSolrJournalName" type="hidden" value=""/>
<input aria-hidden="true" class="hfSolrJournalID" name="hfSolrJournalID" type="hidden" value=""/>
<label for="micrositeSearchTermInputHint-SitePageHeader">
<span class="screenreader-text">Search input auto suggest</span>
</label>
<input autocomplete="off" class="microsite-search-term-input-hint" data-autosuggest-id="micrositeSearchTermInputHint-SitePageHeader" id="micrositeSearchTermInputHint-SitePageHeader" type="text"/>
<ul class="term-list hidden" data-autosuggest-id="micrositeAutoCompleteResults-SitePageHeader"></ul>
</input></div>
<div class="navbar-search-filter_wrap">
<label for="navbar-search-filter-site-SitePageHeader">
<span class="screenreader-text">filter your search</span>
</label>
<select class="navbar-search-filter navbar-search-filter-site at-navbar-search-filter" data-autosuggest-id="search-filter-SitePageHeader" id="navbar-search-filter-site-SitePageHeader">
<option class="header-search-bar-filters-item" data-siteid="0" value="/search-results?page=1&amp;q={searchQuery}">All content</option><option class="header-search-bar-filters-item" data-siteid="3" value="/journals/search-results?page=1&amp;q={searchQuery}&amp;fl_SiteID=3&amp;allJournals=1">All journals</option><option class="header-search-bar-filters-item selected" data-siteid="1000005" selected="" value="/dev/search-results?page=1&amp;q={searchQuery}&amp;fl_SiteID=1000005">Development</option> </select>
</div>
<div class="navbar-search-submit_wrap">
<a class="microsite-search-icon navbar-search-submit icon-menu_search" href="javascript:;"><span class="screenreader-text">Search</span></a>
</div>
</fieldset>
</form><!-- /#MicrositeSearch -->
</div><!-- /.navbar-search -->
<div class="navbar-search-advanced">
<a class="advanced-search" href="/advanced-search">Advanced Search</a>
</div> </div><!-- /.navbar-search-container -->
<input aria-hidden="true" class="hfParentSiteName" name="parentSiteName" type="hidden" value="Journals Gateway"/>
<input aria-hidden="true" class="hfSolrMaxAllowSearchChar" type="hidden" value="100"/>
<input aria-hidden="true" class="hfJournalShortName" type="hidden" value=""/>
<input aria-hidden="true" class="hfSearchPlaceholder" type="hidden" value=""/>
<input aria-hidden="true" class="hfGlobalSearchSiteURL" name="hfGlobalSearchSiteURL" type="hidden" value=""/>
<input aria-hidden="true" id="hfSiteURL" name="hfSearchSiteURL" type="hidden" value="journals.biologists.com/dev"/>
<input aria-hidden="true" class="hfQuickSearchUrl" type="hidden" value="/dev/search-results?page=1&amp;q={searchQuery}&amp;fl_SiteID=1000005"/>
<script type="text/javascript">
        (function () {
            var hfSiteUrl = document.getElementById('hfSiteURL');
            var siteUrl = hfSiteUrl.value;
            var subdomainIndex = siteUrl.indexOf('/');

            hfSiteUrl.value = location.host + (subdomainIndex >= 0 ? siteUrl.substring(subdomainIndex) : '');
        })();
    </script>
<div class="tablet-menu-trigger_wrap">
<!-- MOBILE SHOPPING CART ICON -->
<a aria-controls="tablet-user-dropdown" aria-expanded="false" class="tablet-sign-in" data-theme-dropdown-trigger="tablet-user-dropdown" href="javascript:;"><i class="icon-menu_account"><span class="screenreader-text">User Tools Dropdown</span></i></a>
</div>
<div class="site-theme-header-menu-item_wrap tablet-menu" data-theme-dropdown="tablet-user-dropdown" id="tablet-user-dropdown">
<!-- DESKTOP SHOPPING CART ICON -->
<!-- DESKTOP REGISTRATION -->
<div class="site-theme-header-menu-item"><a class="register at-register js-register-user-modals" href="/my-account/register?siteId=1000005&amp;returnUrl=%2fdev%2fissue%2f151%2f7">Register</a></div>
<!-- DESKTOP INSTITUTIONS -->
<!-- DESKTOP SIGN IN -->
<div class="site-theme-header-menu-item not-authenicated">
<a aria-controls="sign-in-dropdown" aria-expanded="false" class="dropdown-toggle signin at-signin-dropdown at-signin-username" data-login-location="/SignIn/LoginForm/LoginFormPopup?returnUrl=" data-theme-dropdown-trigger="sign-in-dropdown" href="javascript:;" id="header-account-info-user-fullname">

Sign in                <i class="icon-general_arrow-down arrow-icon"></i>
</a>
<div class="dropdown-panel dropdown-panel-signin dropdown-panel-form at-signin-dropdown-panel" data-theme-dropdown="sign-in-dropdown" id="sign-in-dropdown">
<div class="spinner"></div>
</div><!-- /.dropdown-panel -->
</div>
</div>
</div><!-- /.site-theme-header_content -->
</div><!-- /.site-theme-header- -->
<div class="journal-header journal-bg">
<div class="journal-header_content">
<div class="journal-logo_wrap">
<a class="journal-logo-link" href="//journals.biologists.com/dev">
<picture>
<source media="(min-width: 601px)" srcset="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/DEV_title_cropped1750185022.svg"/>
<img alt="Development" class="logo-Development journal-logo" src="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/DEV_title_cropped1750185022.svg"/>
</picture>
</a>
</div>
<div class="navbar-menu_wrap">
<a aria-controls="microsite-nav-menu" aria-expanded="false" class="mobile-site-menu-toggle" data-theme-dropdown-trigger="microsite-nav-menu" href="javascript:;"><i class="icon-menu_hamburger"><span class="screenreader-text">Toggle Menu</span></i><span class="tablet-menu-label">Menu</span></a>
<nav class="navbar-menu" data-theme-dropdown="microsite-nav-menu" id="microsite-nav-menu">
<ul class="site-menu site-menu-lvl-0 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-0" id="site-menu-item-9809">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">Articles<i class="nav-arrow icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9814">
<a class="nav-link" href="/dev/accepted-manuscripts">Accepted manuscripts</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9815">
<a class="nav-link" href="/dev/issue">Latest complete issue</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9816">
<a class="nav-link" href="/dev/issue-covers">Issue archive</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9817">
<a class="nav-link" href="/dev/pages/archive-article-type">Archive by article type</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9818">
<a class="nav-link" href="/dev/pages/special-issues">Special issues</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9819">
<a class="nav-link" href="/dev/../dev/collections">Subject collections</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9820">
<a class="nav-link" href="/dev/pages/alerts">Sign up for alerts</a>
</li>
</ul>
</li>
<li class="site-menu-item site-menu-lvl-0" id="site-menu-item-9810">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">About us<i class="nav-arrow icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9821">
<a class="nav-link" href="/dev/pages/about">About Development</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9822">
<a class="nav-link" href="/dev/pages/about-node">About the Node</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9823">
<a class="nav-link" href="/dev/pages/edboard">Editors and Board</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9824">
<a class="nav-link" href="/dev/pages/editor-bios">Editor biographies</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9825">
<a class="nav-link" href="https://www.biologists.com/travelling-fellowships/">Travelling Fellowships</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9826">
<a class="nav-link" href="https://www.biologists.com/grants/">Grants and funding</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9827">
<a class="nav-link" href="https://www.biologists.com/meetings/">Journal Meetings</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9828">
<a class="nav-link" href="https://www.biologists.com/workshops/">Workshops</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9829">
<a class="nav-link" href="https://www.biologists.com/">The Company of Biologists</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9830">
<a class="nav-link" href="https://forest.biologists.com/">The Forest of Biologists</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9831">
<a class="nav-link" href="/dev/pages/news">Journal news</a>
</li>
</ul>
</li>
<li class="site-menu-item site-menu-lvl-0" id="site-menu-item-9811">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">For authors<i class="nav-arrow icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9832">
<a class="nav-link" href="/dev/pages/submit-manuscript">Submit a manuscript</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9833">
<a class="nav-link" href="/dev/pages/aims">Aims and scope</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9834">
<a class="nav-link" href="/dev/pages/presub-enquiries">Presubmission enquiries</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9835">
<a class="nav-link" href="/dev/pages/article-types">Article types</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9836">
<a class="nav-link" href="/dev/pages/manuscript-prep">Manuscript preparation</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9837">
<a class="nav-link" href="/dev/pages/cover-suggestions">Cover suggestions</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9838">
<a class="nav-link" href="/dev/pages/editorial-process">Editorial process</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9839">
<a class="nav-link" href="/dev/pages/promoting">Promoting your paper</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9840">
<a class="nav-link" href="/dev/pages/open-access">Open Access</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9841">
<a class="nav-link" href="/dev/pages/article-transfer-biology-open">Biology Open transfer</a>
</li>
</ul>
</li>
<li class="site-menu-item site-menu-lvl-0" id="site-menu-item-9812">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">Journal info<i class="nav-arrow icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9842">
<a class="nav-link" href="/dev/pages/journal-policies">Journal policies</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9843">
<a class="nav-link" href="/dev/pages/rights-permissions">Rights and permissions</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9844">
<a class="nav-link" href="/dev/pages/media-policies">Media policies</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9845">
<a class="nav-link" href="/dev/pages/reviewer-guide">Reviewer guide</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9846">
<a class="nav-link" href="/dev/pages/alerts">Sign up for alerts</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9847">
<a class="nav-link" href="https://www.biologists.com/library-hub/">For librarians</a>
</li>
</ul>
</li>
<li class="site-menu-item site-menu-lvl-0" id="site-menu-item-9813">
<a aria-expanded="false" class="nav-link js-theme-dropdown-trigger" href="javascript:;">Contacts<i class="nav-arrow icon-general_arrow-down arrow-icon"></i></a>
<ul class="site-menu site-menu-lvl-1 js-theme-dropdown">
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9848">
<a class="nav-link" href="/dev/pages/contacts">Contacts</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9849">
<a class="nav-link" href="https://www.biologists.com/library-hub">Subscriptions</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9850">
<a class="nav-link" href="https://www.biologists.com/sponsorships-landing-page/">Advertising</a>
</li>
<li class="site-menu-item site-menu-lvl-1" id="site-menu-item-9851">
<a class="nav-link" href="/dev/../contact-us">Feedback</a>
</li>
</ul>
</li>
</ul>
</nav>
</div><!-- /.navbar -->
</div><!-- /.center-inner-row -->
</div><!-- /.journal-header -->
<input id="routename" name="RouteName" type="hidden" value="dev"/>
</div>
</section>
<div class="content-main js-main ui-base" id="main">
<section class="master-main row">
<div class="content-main_content">
<a class="screenreader-text" href="#" id="skipNav" tabindex="-1">Skip Nav Destination</a>
<div class="widget-Lockss widget-instance-IssueBrowseByYear_Lockss">
</div>
<div class="page-column-wrap">
<div class="widget-IssueSelector widget-instance-IssueSelectorRails">
<div class="issue-browse-top issue-dropdown-wrap">
<div class="issue-browse-top_content">
<h1 class="issue-page-title">Issues</h1>
<div class="issue-browse-select_wrap decade">
<div class="issue-browse-decade-nav select-wrap">
<label class="issue-browse-by-year-label" for="DecadeList">Select decade</label>
<div class="single-dropdown-wrap dropdown-decade">
<select class="issue-browse-decade-list issue-browse-select" id="DecadeList">
<option class="issue-browse-option decade-entry" selected="" value="/dev/issue/151/1">2020</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/146/1">2010</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/136/1">2000</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/126/1">1990</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/105/1">1980</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/49/1">1970</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/21/1">1960</option>
<option class="issue-browse-option decade-entry" value="/dev/issue/7/1">1950</option>
</select>
</div>
</div><!-- /.issues-browse-decade-nav -->
<div class="issue-browse-years-nav select-wrap">
<label class="issue-browse-by-year-label" for="YearsList">Select year</label>
<div class="single-dropdown-wrap dropdown-year">
<select class="issue-browse-year-list issue-browse-select at-issue-browse-select-year" id="YearsList">
<option class="issue-browse-option year-entry" selected="" value="/dev/issue/151/1">2024</option>
<option class="issue-browse-option year-entry" value="/dev/issue/150/1">2023</option>
<option class="issue-browse-option year-entry" value="/dev/issue/149/1">2022</option>
<option class="issue-browse-option year-entry" value="/dev/issue/148/1">2021</option>
<option class="issue-browse-option year-entry" value="/dev/issue/147/1">2020</option>
</select>
</div>
</div><!-- /.issue-browse-years-nav -->
<div class="issue-browse-issues-nav select-wrap">
<label class="issue-browse-by-issue-label" for="IssuesList">Issue</label>
<div class="single-dropdown-wrap dropdown-issue">
<select class="issue-browse-issues-list issue-browse-select at-issue-browse-select-issue" id="IssuesList">
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/1">January - Volume 151, Issue 1</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/2">January - Volume 151, Issue 2</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/3">February - Volume 151, Issue 3</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/4">February - Volume 151, Issue 4</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/5">March - Volume 151, Issue 5</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/6">March - Volume 151, Issue 6</option>
<option class="issue-browse-option issue-entry selected" selected="" value="/dev/issue/151/7">April - Volume 151, Issue 7</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/8">April - Volume 151, Issue 8 (In progress)</option>
<option class="issue-browse-option issue-entry selected" value="/dev/issue/151/20">October - Volume 151, Issue 20 (In progress)</option>
</select>
</div>
</div><!-- /.issue-browse-issues-nav -->
</div>
</div>
</div><!-- /.issue-browse-top -->
</div>
<div class="widget-ArticleListAccess widget-instance-ArticleListAccess">
<script type="text/javascript">

        /*******************************************************************************
         * JS here is only being used to assign variables from values in the model
         * logic should be implemented in external JS files, like client.script.js
         *******************************************************************************/

        var SCM = SCM || {};
        var accessIcons = [{"id":346440,"icon":"icon-availability_open","title":"Open Access"},{"id":346516,"icon":"icon-availability_cart","title":"Available to Purchase"},{"id":346512,"icon":"icon-availability_free","title":"Free"},{"id":346436,"icon":"icon-availability_open","title":"Open Access"},{"id":346439,"icon":"icon-availability_cart","title":"Available to Purchase"},{"id":346443,"icon":"icon-availability_free","title":"Free"},{"id":346482,"icon":"icon-availability_free","title":"Free"},{"id":346510,"icon":"icon-availability_free","title":"Free"},{"id":346518,"icon":"icon-availability_free","title":"Free"},{"id":346476,"icon":"icon-availability_open","title":"Open Access"},{"id":346437,"icon":"icon-availability_open","title":"Open Access"},{"id":346477,"icon":"icon-availability_cart","title":"Available to Purchase"},{"id":346520,"icon":"icon-availability_cart","title":"Available to Purchase"},{"id":346438,"icon":"icon-availability_free","title":"Free"},{"id":346475,"icon":"icon-availability_free","title":"Free"},{"id":346511,"icon":"icon-availability_free","title":"Free"},{"id":346517,"icon":"icon-availability_free","title":"Free"},{"id":346509,"icon":"icon-availability_cart","title":"Available to Purchase"},{"id":346555,"icon":"icon-availability_open","title":"Open Access"},{"id":346521,"icon":"icon-availability_cart","title":"Available to Purchase"}];
        if (SCM.AccessIcons) {
            SCM.AccessIcons = SCM.AccessIcons.concat(accessIcons);
        } else {
            SCM.AccessIcons = accessIcons;
        }
        var accessAttributes =  [{"id":346440,"availableforpurchase":false},{"id":346516,"availableforpurchase":true},{"id":346512,"availableforpurchase":false},{"id":346436,"availableforpurchase":false},{"id":346439,"availableforpurchase":true},{"id":346443,"availableforpurchase":false},{"id":346482,"availableforpurchase":false},{"id":346510,"availableforpurchase":false},{"id":346518,"availableforpurchase":false},{"id":346476,"availableforpurchase":false},{"id":346437,"availableforpurchase":false},{"id":346477,"availableforpurchase":true},{"id":346520,"availableforpurchase":true},{"id":346438,"availableforpurchase":false},{"id":346475,"availableforpurchase":false},{"id":346511,"availableforpurchase":false},{"id":346517,"availableforpurchase":false},{"id":346509,"availableforpurchase":true},{"id":346555,"availableforpurchase":false},{"id":346521,"availableforpurchase":true}];
        if (SCM.AccessAttributes) {
            SCM.AccessAttributes = SCM.AccessAttributes.concat(accessAttributes);
        } else {
            SCM.AccessAttributes = accessAttributes;
        }

    </script>
</div>
<div class="issue-browse_content">
<div class="issue-browse-left-nav page-column page-column--left" id="InfoColumn">
<div class="info-inner-wrap can-stick">
<div class="info-widget-wrap article-issue-info">
<div class="widget-IssueInfo widget-instance-IssueOnRails_IssueInfoOnRails">
<div class="article-info-wrap clearfix issue-info-rails">
<div class="volume-issue__wrap">
<a href="/dev/issue/151/7">
<span class="volume issue">Volume 151, Issue 7</span>
</a>
</div><div class="ii-pub-date">
April 2024</div>
<div class="article-issue-img">
<a href="/dev/issue/151/7">
<img alt="Issue Cover" class="fb-featured-image at-coverimage" id="issueImage" src="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/m_develop_151_7.cover.png?Expires=1716971121&amp;Signature=Q5BMOwliVwZ9-uHXmZtPRsqXibeH5AaG5fJqZltbnYkBmZKipgBNZWE2bO0ecXWEKGA0bH90tktgdmeZWjh2IEyb-Hh5M7ieNQ8iH0Nr1TD6yGEPSJTv29PkLni~QbV-cbsj9cz21kQfh66SvYcvu9xjFtinG93ANKFDkIJkXbwliQ2rdj~EjslykrOBNnC9E3lXebY8-Px4wjwlMV0O4siYE0Yf0ITR3KwQhTSfBHARuKNCMH7jbCmaT~IrgGposDgrYanl0Xx~Kq8zOTCtP~hjeDaLvsUUdMN8LtdDgadfqD-MBWC90N4TvksbMt-Q5u-G~FI9gO15Oq2BZ33QQQ__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"/>
</a>
</div> <ul class="inline-list">
<li class="previous arrow">
<a href="/dev/issue/151/6"><i class="icon-general_arrow-left"></i>Previous issue</a>
</li>
<li class="next arrow">
<a href="/dev/issue/151/8">Next issue<i class="icon-general_arrow-right"></i></a>
</li>
</ul>
<div class="widget-AllIssuesLink widget-instance-IssueOnRails_IssueInfoOnRails">
<div class="all-issues-link">
<a href="/dev/issue-covers">All issues</a>
</div>
</div>
<div class="widget-IssueSupplementalLinks widget-instance-IssueOnRails_IssueInfoOnRails">
<!-- Supplemental links-->
<div class="issue-supplemental-link-list-wrap">
<ul class="issue-supplemental-link-list left-rail">
<li>
<a data-modal-source-id="cover-modal" href="javascript:;">
<span>Cover image</span>
</a>
<div class="modal-only-content" data-content-id="cover-modal">
<h4>Cover Image</h4>
<div class="IssueCoverFigure">
<img alt="issue cover" class="lazy" data-src="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/develop_151_7.coverfig.png?Expires=1716971121&amp;Signature=BsF8IkhhyM2Ts~E914sW1Cz2GL~xpyqz6bQBqgcI6tOg2lGnv3f-I8LjCAzidxMFXj3nPD8d2o2IGx8rgYRyUC~y8gdTKGtBcS8eBiyb45Zb23pJBZkwuqnsDuh6emzN~mevQxvxGxSg4-2ebfKIGeU~4UIg~CxmOIEulnz2SUupfNLjvRYoUNdr~HMfyVZUZJ1Kfm8I6EH~DS6HDRC3zwAzGycRXMeQM8~dVRL1DHcxzj7lMd4iltVf7THzEAEx4H3kENhHlUAaE-IjhZ4LP2HLi5LyQPrNszHhWolCJErmfiKEO7jeKRhQxNwPe3rK~CipymlK-eBV-3jD5~jPiA__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" src="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/develop_151_7.coverfig.png?Expires=1716971121&amp;Signature=BsF8IkhhyM2Ts~E914sW1Cz2GL~xpyqz6bQBqgcI6tOg2lGnv3f-I8LjCAzidxMFXj3nPD8d2o2IGx8rgYRyUC~y8gdTKGtBcS8eBiyb45Zb23pJBZkwuqnsDuh6emzN~mevQxvxGxSg4-2ebfKIGeU~4UIg~CxmOIEulnz2SUupfNLjvRYoUNdr~HMfyVZUZJ1Kfm8I6EH~DS6HDRC3zwAzGycRXMeQM8~dVRL1DHcxzj7lMd4iltVf7THzEAEx4H3kENhHlUAaE-IjhZ4LP2HLi5LyQPrNszHhWolCJErmfiKEO7jeKRhQxNwPe3rK~CipymlK-eBV-3jD5~jPiA__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"/>
</div>
<div class="IssueCoverCaption">
<p><b>Cover:</b> Scanning electron microscopy image depicting macrophages forming a crown-like structure (pseudocoloured in green) around histolyzing larval adipocytes in freshly eclosed <i>Drosophila melanogaster</i>. At this stage, macrophages recycle matter from adipocytes and convert it into nutrients used by maturing adult tissues. See Research article by KrejÄovÃ¡ et al. (<a href="https://journals.biologists.com/dev/article-lookup/doi/10.1242/dev.202492">dev.202492</a>).</p>
</div>
</div>
</li>
<li>
<i class="icon-menu_pdf"><span class="screenreader-text">PDF Icon</span></i>
<a class="al-link pdf article-pdfLink openInAnotherWindow js-download-file-gtm-datalayer-event" data-doctype="issueEdBoardPdf" data-issueno="7" data-volume="151" href="https://cob.silverchair-cdn.com/cob/content_public/journal/dev/issue/151/7/16/ed_board.pdf?Expires=1716971121&amp;Signature=TItcb9WWZGtSNowBMiPiwU4B1sK0bT6sAjvEUaCQH58wfYYO29MzSwlnjEy1tdBZDZkXhvdiXDh1I4z07EsJlVonQnJ4cNWBSIwLN1VkoyFMo~LQXu2Ya~e-z0eRSzGjktBO-UFb3TSibZGKLrFjKh-5Lz~PXZHeQCXyKbC7t4PxAaXnPIXyviOq6krPHYD7wDBvEX3P2NSvV0RacmiVPZAjjeL0LNc6Tim0k16O3pA960oY08rFjnsTk5U6FgwLqnZXYpRiIiDnZ6FR1PM2Ax1U5YNqmIPwMs-CLFyKEWJqmSSeSUbaWx42mq0wq~1C8hUKvEnoli7tVeTMfcwh5Q__&amp;Key-Pair-Id=APKAIE5G5CRDK6RD3PGA" target="_blank">
<i class="icon-file-pdf-small"><span class="screenreader-text">PDF Link</span></i><span>Issue info</span>
</a>
</li>
</ul>
</div> <!-- /Supplemental links-->
</div>
<div class="issue-info-details">
<div class="issue-info-ISSN">ISSN 0950-1991</div>
<div class="issue-info-EISSN">EISSN 1477-9129</div>
</div>
<div class="widget-IssueJumpLinks widget-instance-IssueOnRails_IssueJumpLinks">
<div class="responsive-issue-nav" id="scrollMenu">
<button class="toggle-left-col__close btn-as-icon icon-general-close" type="button">
<span class="screenreader-text">Close navigation menu</span>
</button>
<div class="in-this-issue-title">In this issue</div>
<!--desktop / tablet navigation -->
<ul class="artTypeJumpLinks list-issue-jumplinks" id="largeJumptoSection">
<li class="section-jump-link parent" data-level="1" link-destination="107436-346443">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107436-346443">RESEARCH HIGHLIGHTS</a>
</div>
</li>
<li class="section-jump-link parent" data-level="1" link-destination="107437-346517">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107437-346517">INTERVIEWS</a>
</div>
</li>
<li class="section-jump-link parent" data-level="1" link-destination="107438-346436">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107438-346436">SPOTLIGHT</a>
</div>
</li>
<li class="section-jump-link parent" data-level="1" link-destination="107439-346555">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107439-346555">REVIEW</a>
</div>
</li>
<li class="section-jump-link parent" data-level="1" link-destination="107440-346437">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107440-346437">RESEARCH REPORT</a>
</div>
</li>
<li class="section-jump-link parent" data-level="1" link-destination="107441-346476">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107441-346476">RESEARCH ARTICLES</a>
</div>
</li>
<li class="section-jump-link parent" data-level="1" link-destination="107442-346477">
<div class="section-jump-link__link-wrap viewView">
<a class="jumplink scrollTo" href="#107442-346477">TECHNIQUES AND RESOURCES</a>
</div>
</li>
</ul>
</div><!-- /#scrollMenu -->
</div>
</div>
</div>
</div>
</div><!-- /.info-inner-wrap -->
</div><!-- /#InfoColumn .page-column-/-left -->
<div class="page-column page-column--center center-content can-stick" id="ContentColumn">
<div class="widget-Issue">
<div class="issue-browse-top issue-browse-mobile-nav">
<button class="btn toggle-left-col toggle-left-col__issue" type="button">Issue Navigation</button>
</div><!-- /.issue-browse-top .issue-browse-mobile-nav -->
<div class="content-inner-wrap">
<div class="widget-DynamicWidgetLayout widget-instance-Issue_TopRail">
<div class="widget widget-dynamic" data-count="0">
<div class="widget-dynamic-inner-wrap">
</div>
</div>
</div>
<div id="ArticleList">
<div class="widget-IssueArticleList widget-instance-IssueOnRails_IssueArticleList">
<div class="article-list-resources" id="resourceTypeList-IssueOnRails_IssueArticleList">
<div class="section-container">
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107436-346443" data-section-title="" id="107436-346443">
                RESEARCH HIGHLIGHTS
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346443">
<a href="/dev/article/151/7/e151_e0701/346443/Macrophages-more-than-just-engulfing-dying-cells">Macrophages: more than just engulfing dying cells</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract extract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346443" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="extract" data-articleid="346443" data-is-lay-abstract="False" href="javascript:;">
Extract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346443">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/e151_e0701/346443/Macrophages-more-than-just-engulfing-dying-cells">View article<span class="screenreader-text">titled, Macrophages: more than just engulfing dying cells</span></a></div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346443"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346482">
<a href="/dev/article/151/7/e151_e0702/346482/Cadherin-based-adhesions-put-MuSCs-in-place">Cadherin-based adhesions put MuSCs in place</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract extract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346482" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="extract" data-articleid="346482" data-is-lay-abstract="False" href="javascript:;">
Extract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346482">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/e151_e0702/346482/Cadherin-based-adhesions-put-MuSCs-in-place">View article<span class="screenreader-text">titled, Cadherin-based adhesions put MuSCs in place</span></a></div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346482"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346512">
<a href="/dev/article/151/7/e151_e0703/346512/Depleting-key-nutrients-presses-pause-on-embryonic">Depleting key nutrients presses pause on embryonic development</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract extract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346512" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="extract" data-articleid="346512" data-is-lay-abstract="False" href="javascript:;">
Extract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346512">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/e151_e0703/346512/Depleting-key-nutrients-presses-pause-on-embryonic">View article<span class="screenreader-text">titled, Depleting key nutrients presses pause on embryonic development</span></a></div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346512"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346518">
<a href="/dev/article/151/7/e151_e0704/346518/Timing-matters-Aurora-A-in-cell-polarization">Timing matters: Aurora A in cell polarization</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract extract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346518" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="extract" data-articleid="346518" data-is-lay-abstract="False" href="javascript:;">
Extract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346518">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/e151_e0704/346518/Timing-matters-Aurora-A-in-cell-polarization">View article<span class="screenreader-text">titled, Timing matters: Aurora A in cell polarization</span></a></div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346518"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107437-346517" data-section-title="" id="107437-346517">
                INTERVIEWS
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346517">
<a href="/dev/article/151/7/dev202889/346517/The-people-behind-the-papers-Nadia-Manzi-and">The people behind the papers – Nadia Manzi and Daniel Dickinson</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346517" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346517" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346517">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202889/346517/The-people-behind-the-papers-Nadia-Manzi-and">View article<span class="screenreader-text">titled, The people behind the papers – Nadia Manzi and Daniel Dickinson</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346517" data-doctype="contentPdf" data-doi="10.1242/dev.202889" data-resourceid="346517" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202889/3415209/dev202889.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346517"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346511">
<a href="/dev/article/151/7/dev202869/346511/The-people-behind-the-papers-Jiajia-Ye-and-Qiang">The people behind the papers – Jiajia Ye and Qiang Sun</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346511" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346511" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346511">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202869/346511/The-people-behind-the-papers-Jiajia-Ye-and-Qiang">View article<span class="screenreader-text">titled, The people behind the papers – Jiajia Ye and Qiang Sun</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346511" data-doctype="contentPdf" data-doi="10.1242/dev.202869" data-resourceid="346511" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202869/3415157/dev202869.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346511"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346510">
<a href="/dev/article/151/7/dev202840/346510/Transitions-in-development-an-interview-with">Transitions in development – an interview with Rajendhran Rajakumar</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346510" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346510" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346510">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202840/346510/Transitions-in-development-an-interview-with">View article<span class="screenreader-text">titled, Transitions in development – an interview with Rajendhran Rajakumar</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346510" data-doctype="contentPdf" data-doi="10.1242/dev.202840" data-resourceid="346510" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202840/3414990/dev202840.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346510"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346475">
<a href="/dev/article/151/7/dev202888/346475/The-people-behind-the-papers-Margaret-Hung-and">The people behind the papers – Margaret Hung and Robert Krauss</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346475" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346475" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346475">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202888/346475/The-people-behind-the-papers-Margaret-Hung-and">View article<span class="screenreader-text">titled, The people behind the papers – Margaret Hung and Robert Krauss</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346475" data-doctype="contentPdf" data-doi="10.1242/dev.202888" data-resourceid="346475" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202888/3414607/dev202888.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346475"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346438">
<a href="/dev/article/151/7/dev202859/346438/The-people-behind-the-papers-Gabriela-Krejcova-and">The people behind the papers – Gabriela Krejčová and Adam Bajgar</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-article-synopsis">
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346438" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346438" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346438">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202859/346438/The-people-behind-the-papers-Gabriela-Krejcova-and">View article<span class="screenreader-text">titled, The people behind the papers – Gabriela Krejčová and Adam Bajgar</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346438" data-doctype="contentPdf" data-doi="10.1242/dev.202859" data-resourceid="346438" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202859/3415398/dev202859.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346438"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107438-346436" data-section-title="" id="107438-346436">
                SPOTLIGHT
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346436">
<a href="/dev/article/151/7/dev202067/346436/Clinical-translation-of-pluripotent-stem-cell">Clinical translation of pluripotent stem cell-based therapies: successes and challenges</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Josefine+R%c3%a5g%c3%a5rd+Christiansen">Josefine Rågård Christiansen</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Agnete+Kirkeby">Agnete Kirkeby</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Great advancements have been made in recent years to bring pluripotent stem cell-based therapies to the clinic. This Spotlight highlights promising clinical results and discusses challenges associated with clinical translation.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346436" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346436" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346436">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202067/346436/Clinical-translation-of-pluripotent-stem-cell">View article<span class="screenreader-text">titled, Clinical translation of pluripotent stem cell-based therapies: successes and challenges</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346436" data-doctype="contentPdf" data-doi="10.1242/dev.202067" data-resourceid="346436" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202067/3414164/dev202067.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346436"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107439-346555" data-section-title="" id="107439-346555">
                REVIEW
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346555">
<a href="/dev/article/151/7/dev201102/346555/The-journey-of-a-generation-advances-and-promises">The journey of a generation: advances and promises in the study of primordial germ cell migration</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Lacy+J.+Barton">Lacy J. Barton</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Lorena+Roa-de+la+Cruz">Lorena Roa-de la Cruz</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Ruth+Lehmann">Ruth Lehmann</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Benjamin+Lin">Benjamin Lin</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> This Review covers the mechanisms of primordial germ cell migration in model organisms and systems, emphasizing the guidance factors and signaling pathways necessary for colonization of the gonad.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346555" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346555" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346555">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev201102/346555/The-journey-of-a-generation-advances-and-promises">View article<span class="screenreader-text">titled, The journey of a generation: advances and promises in the study of primordial germ cell migration</span></a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346555" data-doctype="contentPdf" data-doi="10.1242/dev.201102" data-resourceid="346555" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.201102/3416290/dev201102.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346555"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107440-346437" data-section-title="" id="107440-346437">
                RESEARCH REPORT
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346437">
<a href="/dev/article/151/7/dev202370/346437/The-Shot-CH1-domain-recognises-a-distinct-form-of">The Shot CH1 domain recognises a distinct form of F-actin during <em>Drosophila</em> oocyte determination</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Dmitry+Nashchekin">Dmitry Nashchekin</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Iolo+Squires">Iolo Squires</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Andreas+Prokop">Andreas Prokop</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Daniel+St+Johnston">Daniel St Johnston</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Actin filaments in a specific conformational state are formed during oocyte fate establishment in <em>Drosophila</em>, and they are recognised only by a subset of actin-binding proteins.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346437" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346437" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346437">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202370/346437/The-Shot-CH1-domain-recognises-a-distinct-form-of">View article<span class="screenreader-text">titled, The Shot CH1 domain recognises a distinct form of F-actin during &lt;em&gt;Drosophila&lt;/em&gt; oocyte determination</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202370/346437/The-Shot-CH1-domain-recognises-a-distinct-form-of#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346437" data-doctype="contentPdf" data-doi="10.1242/dev.202370" data-resourceid="346437" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202370/3414169/dev202370.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346437"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107441-346476" data-section-title="" id="107441-346476">
                RESEARCH ARTICLES
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346476">
<a href="/dev/article/151/7/dev202387/346476/Cadherin-dependent-adhesion-is-required-for-muscle">Cadherin-dependent adhesion is required for muscle stem cell niche anchorage and maintenance</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Margaret+Hung">Margaret Hung</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Hsiao-Fan+Lo">Hsiao-Fan Lo</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Aviva+G.+Beckmann">Aviva G. Beckmann</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Deniz+Demircioglu">Deniz Demircioglu</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Gargi+Damle">Gargi Damle</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Dan+Hasson">Dan Hasson</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Glenn+L.+Radice">Glenn L. Radice</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Robert+S.+Krauss">Robert S. Krauss</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Genetic ablation of cadherin-based adhesion in skeletal muscle stem cells triggers activation, niche exit, precocious differentiation and subsequent depletion of the stem cell pool.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346476" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346476" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346476">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202387/346476/Cadherin-dependent-adhesion-is-required-for-muscle">View article<span class="screenreader-text">titled, Cadherin-dependent adhesion is required for muscle stem cell niche anchorage and maintenance</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202387/346476/Cadherin-dependent-adhesion-is-required-for-muscle#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346476" data-doctype="contentPdf" data-doi="10.1242/dev.202387" data-resourceid="346476" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202387/3415435/dev202387.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346476"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346521">
<a href="/dev/article/151/7/dev202371/346521/Apical-expansion-of-calvarial-osteoblasts-and">Apical expansion of calvarial osteoblasts and suture patency is dependent on fibronectin cues</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Xiaotian+Feng">Xiaotian Feng</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Helen+Molteni">Helen Molteni</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Megan+Gregory">Megan Gregory</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Jennifer+Lanza">Jennifer Lanza</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Nikaya+Polsani">Nikaya Polsani</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Isha+Gupta">Isha Gupta</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Rachel+Wyetzner">Rachel Wyetzner</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=M.+Brent+Hawkins">M. Brent Hawkins</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Greg+Holmes">Greg Holmes</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Sevan+Hopyan">Sevan Hopyan</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Matthew+P.+Harris">Matthew P. Harris</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Radhika+P.+Atit">Radhika P. Atit</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Fibronectin matrix substrate couples apical growth of frontal bone and coronal suture patency in early embryonic development, leading to calvarial pathologies when disrupted.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346521" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346521" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346521">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202371/346521/Apical-expansion-of-calvarial-osteoblasts-and">View article<span class="screenreader-text">titled, Apical expansion of calvarial osteoblasts and suture patency is dependent on fibronectin cues</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202371/346521/Apical-expansion-of-calvarial-osteoblasts-and#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346521" data-doctype="contentPdf" data-doi="10.1242/dev.202371" data-resourceid="346521" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202371/3415293/dev202371.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346521"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346520">
<a href="/dev/article/151/7/dev202608/346520/CFAP58-is-involved-in-the-sperm-head-shaping-and">CFAP58 is involved in the sperm head shaping and flagellogenesis of cattle and mice</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Xiaochao+Wei">Xiaochao Wei</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Xiuge+Wang">Xiuge Wang</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Chunhong+Yang">Chunhong Yang</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yaping+Gao">Yaping Gao</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yaran+Zhang">Yaran Zhang</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yao+Xiao">Yao Xiao</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Zhihua+Ju">Zhihua Ju</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Qiang+Jiang">Qiang Jiang</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Jinpeng+Wang">Jinpeng Wang</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Wenhao+Liu">Wenhao Liu</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yanqin+Li">Yanqin Li</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yundong+Gao">Yundong Gao</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Jinming+Huang">Jinming Huang</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Analysis of genetic variants of bovine <em>CFAP58</em> and loss of <em>Cfap58</em> in mice reveals that CFAP58 is required for correct development of manchette structure during spermatogenesis, thereby affecting male fertility.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346520" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346520" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346520">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202608/346520/CFAP58-is-involved-in-the-sperm-head-shaping-and">View article<span class="screenreader-text">titled, CFAP58 is involved in the sperm head shaping and flagellogenesis of cattle and mice</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202608/346520/CFAP58-is-involved-in-the-sperm-head-shaping-and#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346520" data-doctype="contentPdf" data-doi="10.1242/dev.202608" data-resourceid="346520" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202608/3415275/dev202608.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346520"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346516">
<a href="/dev/article/151/7/dev202479/346516/Temporally-distinct-roles-of-Aurora-A-in">Temporally distinct roles of Aurora A in polarization of the <em>C. elegans</em> zygote</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Nadia+I.+Manzi">Nadia I. Manzi</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Bailey+N.+de+Jesus">Bailey N. de Jesus</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yu+Shi">Yu Shi</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Daniel+J.+Dickinson">Daniel J. Dickinson</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><span class="related-article"><a data-page="e151_e0704" data-vol="151" href="https://journals.biologists.com/dev/article/151/7/dev202479/346516/Temporally-distinct-roles-of-Aurora-A-in"><strong>Highlighted Article:</strong></a></span> The cell cycle kinase Aurora A has two distinct roles in regulating the timing of cell polarization: a late role required for symmetry breaking, and an earlier function that ensures a unique polarity axis.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346516" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346516" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346516">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202479/346516/Temporally-distinct-roles-of-Aurora-A-in">View article<span class="screenreader-text">titled, Temporally distinct roles of Aurora A in polarization of the &lt;em&gt;C. elegans&lt;/em&gt; zygote</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202479/346516/Temporally-distinct-roles-of-Aurora-A-in#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346516" data-doctype="contentPdf" data-doi="10.1242/dev.202479" data-resourceid="346516" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202479/3415238/dev202479.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346516"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346509">
<a href="/dev/article/151/7/dev202091/346509/Nutrient-deprivation-induces-mouse-embryonic">Nutrient deprivation induces mouse embryonic diapause mediated by Gator1 and Tsc2</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Jiajia+Ye">Jiajia Ye</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yuting+Xu">Yuting Xu</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Qi+Ren">Qi Ren</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Lu+Liu">Lu Liu</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Qiang+Sun">Qiang Sun</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><span class="related-article"><a data-page="e151_e0703" data-vol="151" href="https://journals.biologists.com/dev/article/151/7/dev202091/346509/Nutrient-deprivation-induces-mouse-embryonic"><strong>Highlighted Article:</strong></a></span> Mouse embryonic diapause is induced by either decreased concentration of several nutrients in the uterine fluid of mice suffering from pre-implantation maternal starvation <em>in vivo</em> or nutrient deprivation <em>in vitro</em>.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346509" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346509" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346509">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202091/346509/Nutrient-deprivation-induces-mouse-embryonic">View article<span class="screenreader-text">titled, Nutrient deprivation induces mouse embryonic diapause mediated by Gator1 and Tsc2</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202091/346509/Nutrient-deprivation-induces-mouse-embryonic#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346509" data-doctype="contentPdf" data-doi="10.1242/dev.202091" data-resourceid="346509" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202091/3415129/dev202091.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346509"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346440">
<a href="/dev/article/151/7/dev202546/346440/Foxp-and-Skor-family-proteins-control">Foxp and Skor family proteins control differentiation of Purkinje cells from Ptf1a- and Neurog1-expressing progenitors in zebrafish</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Tsubasa+Itoh">Tsubasa Itoh</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Mari+Uehara">Mari Uehara</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Shinnosuke+Yura">Shinnosuke Yura</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Jui+Chun+Wang">Jui Chun Wang</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Yukimi+Fujii">Yukimi Fujii</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Akiko+Nakanishi">Akiko Nakanishi</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Takashi+Shimizu">Takashi Shimizu</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Masahiko+Hibi">Masahiko Hibi</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Analysis of zebrafish mutants and lineage tracing of <em>ptf1a</em>-expressing progenitors reveal that Foxp and Skor family transcriptional regulators control the differentiation of Purkinje cells from neural progenitors expressing the proneural genes <em>ptf1a</em> and <em>neurog1</em>.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346440" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346440" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346440">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202546/346440/Foxp-and-Skor-family-proteins-control">View article<span class="screenreader-text">titled, Foxp and Skor family proteins control differentiation of Purkinje cells from Ptf1a- and Neurog1-expressing progenitors in zebrafish</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202546/346440/Foxp-and-Skor-family-proteins-control#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346440" data-doctype="contentPdf" data-doi="10.1242/dev.202546" data-resourceid="346440" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202546/3414205/dev202546.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346440"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346439">
<a href="/dev/article/151/7/dev202492/346439/Macrophages-play-a-nutritive-role-in-post">Macrophages play a nutritive role in post-metamorphic maturation in <em>Drosophila</em></a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Gabriela+Krej%c4%8dov%c3%a1">Gabriela Krejčová</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Ad%c3%a9la+Danielov%c3%a1">Adéla Danielová</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Hana+Sehadov%c3%a1">Hana Sehadová</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Filip+Dy%c4%8dka">Filip Dyčka</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Ji%c5%99%c3%ad+Kub%c3%a1sek">Jiří Kubásek</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Martin+Moos">Martin Moos</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Adam+Bajgar">Adam Bajgar</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><span class="related-article"><a data-page="e151_e0701" data-vol="151" href="https://journals.biologists.com/dev/article/151/7/dev202492/346439/Macrophages-play-a-nutritive-role-in-post"><strong>Highlighted Article:</strong></a></span> Macrophages adopt a unique metabolic profile to convert engulfed cell mass into lipoproteins and storage peptides that metabolically supplement other tissues during post-metamorphic maturation in <em>Drosophila</em>.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346439" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346439" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346439">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202492/346439/Macrophages-play-a-nutritive-role-in-post">View article<span class="screenreader-text">titled, Macrophages play a nutritive role in post-metamorphic maturation in &lt;em&gt;Drosophila&lt;/em&gt;</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202492/346439/Macrophages-play-a-nutritive-role-in-post#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346439" data-doctype="contentPdf" data-doi="10.1242/dev.202492" data-resourceid="346439" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202492/3414303/dev202492.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346439"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
<section>
<h4 class="title articleClientType act-header" data-level="1" data-magellan-destination="107442-346477" data-section-title="" id="107442-346477">
                TECHNIQUES AND RESOURCES
            </h4>
<div class="content al-article-list-group" data-section-content="">
<div class="al-article-item-wrap al-normal">
<div class="al-article-items">
<h5 class="customLink item-title" data-resource-id-access="346477">
<a href="/dev/article/151/7/dev202614/346477/A-multistep-computational-approach-reveals-a-neuro">A multistep computational approach reveals a neuro-mesenchymal cell population in the embryonic hematopoietic stem cell niche</a>
<i class="js-access-icon-placeholder"></i>
</h5><!-- /.customLink -->
<div class="al-authors-list">
<span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Olivera+Miladinovic">Olivera Miladinovic</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Pierre-Yves+Canto">Pierre-Yves Canto</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Claire+Pouget">Claire Pouget</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Olivier+Piau">Olivier Piau</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Nevenka+Radic">Nevenka Radic</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Priscilla+Freschu">Priscilla Freschu</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Alexandre+Megherbi">Alexandre Megherbi</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Carla+Brujas+Prats">Carla Brujas Prats</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Sebastien+Jacques">Sebastien Jacques</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Estelle+Hirsinger">Estelle Hirsinger</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Audrey+Geeverding">Audrey Geeverding</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Sylvie+Dufour">Sylvie Dufour</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Laurence+Petit">Laurence Petit</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Michele+Souyri">Michele Souyri</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Trista+North">Trista North</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Herv%c3%a9+Isambert">Hervé Isambert</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=David+Traver">David Traver</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Thierry+Jaffredo">Thierry Jaffredo</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Pierre+Charbord">Pierre Charbord</a></span><span class="al-author-delim">,</span><span class="wi-fullname brand-fg"><a href="/dev/search-results?f_AllAuthors=Charles+Durand">Charles Durand</a></span>
</div>
<div class="al-article-synopsis">
<section class="abstract"><p><strong>Summary:</strong> Identification of a previously undescribed neuro-mesenchymal cell population in the embryonic hematopoietic stem cell niche through multi-layered transcriptomics and computational analyses.</p></section>
</div>
<div class="badge-bar">
<div class="resource-links-info">
<div class="item"><!-- Widget:ArticleAbstract Instance: -->
<!-- Widget:ArticleAbstract Instance: -->
<div class="resource-link resource-abstract abstract">
<div class="abstract al-other-resource-links abstract-link">
<a aria-controls="abstract-346477" aria-expanded="false" class="showAbstractLink js-show-abstract at-Show-Abstract-Link" data-abstract-type="abstract" data-articleid="346477" data-is-lay-abstract="False" href="javascript:;">
Abstract            <i class="abstract-toggle-icon js-abstract-toggle-icon icon-general_arrow-down" data-icon-class="icon-general_arrow"></i>
</a>
</div>
</div>
<div aria-hidden="true" class="abstract-response-placeholder js-abstract-response-placeholder hide" id="abstract-346477">
<div class="loading js-loading"></div>
</div>
</div>
<div class="item"><a class="viewArticleLink" href="/dev/article/151/7/dev202614/346477/A-multistep-computational-approach-reveals-a-neuro">View article<span class="screenreader-text">titled, A multistep computational approach reveals a neuro-mesenchymal cell population in the embryonic hematopoietic stem cell niche</span></a></div>
<div class="item"><a class="SupplementaryDataLink" href="/dev/article/151/7/dev202614/346477/A-multistep-computational-approach-reveals-a-neuro#supplementary-data">Supplementary information</a></div>
<div class="item">
<a class="al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink" data-article-id="346477" data-doctype="contentPdf" data-doi="10.1242/dev.202614" data-resourceid="346477" data-resourcetypeid="Article" href="/dev/article-pdf/doi/10.1242/dev.202614/3414624/dev202614.pdf" target="_blank">
<span class="screenreader-text">Open the </span>
<i class="icon-menu_pdf-small">
</i><span>PDF <span class="screenreader-text">for  in another window</span></span>
</a>
</div>
</div>
</div>
<div class="al-expanded-section" hidden="" id="target346477"></div>
</div><!-- /.al-article-items -->
</div><!-- /al-article-item-wrap al-normal -->
</div>
</section>
</div>
</div>
</div>
</div><!-- /#ArticleList -->
</div><!-- /.content-inner-wrap -->
</div><!-- /.widget-issue -->
</div><!-- /#ContentColumn --><div class="page-column page-column--right issue-sidebar" id="Sidebar">
<div class="sidebar-widget_wrap">
<div class="widget-DynamicWidgetLayout widget-instance-Issue_RightRail">
<div class="widget widget-dynamic" data-count="1">
<div class="widget-dynamic-inner-wrap">
<div class="widget-DynamicWidgetLayout widget-instance-Issue_RightRailB0">
<div class="widget widget-dynamic right-rail" data-count="4">
<div class="widget-dynamic-inner-wrap">
<div class="widget-DynamicWidgetLayout widget-instance-Issue_RightRailB0B0">
<div class="widget widget-dynamic issue-alerts" data-count="1">
<div class="widget-dynamic-inner-wrap">
<div class="widget-Alerts widget-instance-Issue_RightRailB0B0Issue_Alerts">
<div class="widget widget-alerts rail-widget_wrap vt-widget-alerts" id="alerts">
<h3 class="alerts-widget-header">Email alerts</h3>
<div class="widget-links_wrap">
<div class="userAlert alertType-3">
<a class="js-open-alert-modal" data-alert-type="3" data-user-logged-in="False" href="javascript:;">Accepted manuscripts alert</a>
</div>
<div class="userAlert alertType-23">
<a class="js-open-alert-modal" data-alert-type="23" data-user-logged-in="False" href="javascript:;">Table of contents alert</a>
</div>
<div class="userAlert alertType-30">
<a class="js-open-alert-modal" data-alert-type="30" data-user-logged-in="False" href="javascript:;">Latest published articles alert</a>
</div>
<div class="userAlertSignUpModal reveal-modal small" data-reveal="">
<div class="userAlertSignUp"></div>
<a class="close-reveal-modal js-close-modal" href="javascript:;"><i class="icon-general-close"><span class="screenreader-text">Close Modal</span></i></a>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="widget-DynamicWidgetLayout widget-instance-Issue_RightRailB0B1">
<div class="widget widget-dynamic issue-selectablecontentlist" data-count="1">
<div class="widget-dynamic-inner-wrap">
<div class="widget-SelectableContentList widget-instance-Issue_RightRailB0B1issue-SelectableContentList">
<div class="widget-dynamic-content basic-view">
<div class="widget-dynamic-heading">
        Accepted manuscripts
    </div>
<div class="widget-dynamic-entry-wrap">
<div class="widget-dynamic-entry item at-widget-entry-SCL">
<span aria-hidden="true" class="hfDoi" data-attribute="10.1242/dev.202292"></span>
<div class="widget-dynamic-content-wrap">
<div class="widget-dynamic-journal-title">
<a href="/dev/article/doi/10.1242/dev.202292/347001/Foxg1-bimodally-tunes-L1-mRNA-and-DNA-dynamics-in">
                    Foxg1  bimodally tunes  L1 -mRNA and -DNA dynamics in the developing murine neocortex
                </a>
</div>
<div class="widget-dynamic-journal-authors">
                Gabriele Liuzzi, Osvaldo Artimagnella, Simone Frisari, Antonello Mallamaci
            </div>
</div>
</div>
<div class="widget-dynamic-entry item at-widget-entry-SCL">
<span aria-hidden="true" class="hfDoi" data-attribute="10.1242/dev.202518"></span>
<div class="widget-dynamic-content-wrap">
<div class="widget-dynamic-journal-title">
<a href="/dev/article/doi/10.1242/dev.202518/346893/E93-is-indispensable-for-reproduction-in">
                    E93 is indispensable for reproduction in ametabolous and hemimetabolous insects
                </a>
</div>
<div class="widget-dynamic-journal-authors">
                Yu Bai, Ya-Nan Lv, Mei Zeng, Zi-Yu Yan, Dan-Yan Huang, Jia-Zhen Wen, Hu-Na Lu, Pei-Yan Zhang, Yi-Fan Wang, Ning Ban, Dong-Wei Yuan, Sheng Li, Yun-Xia Luan
            </div>
</div>
</div>
<div class="widget-dynamic-entry item at-widget-entry-SCL">
<span aria-hidden="true" class="hfDoi" data-attribute="10.1242/dev.202262"></span>
<div class="widget-dynamic-content-wrap">
<div class="widget-dynamic-journal-title">
<a href="/dev/article/doi/10.1242/dev.202262/346894/Two-sequential-gene-expression-programs-bridged-by">
                    Two sequential gene expression programs bridged by cell division support long-distance collective cell migration
                </a>
</div>
<div class="widget-dynamic-journal-authors">
                Jingjing Sun, Ayse Damla Durmaz, Aswini Babu, Frank Macabenta, Angelike Stathopoulos
            </div>
</div>
</div>
<div class="widget-dynamic-entry item at-widget-entry-SCL">
<span aria-hidden="true" class="hfDoi" data-attribute="10.1242/dev.202862"></span>
<div class="widget-dynamic-content-wrap">
<div class="widget-dynamic-journal-title">
<a href="/dev/article/doi/10.1242/dev.202862/346876/Mechanical-stress-combines-with-planar-polarised">
                    Mechanical stress combines with planar polarised patterning during metaphase to orient embryonic epithelial cell divisions
                </a>
</div>
<div class="widget-dynamic-journal-authors">
                Guy B. Blanchard, Elena Scarpa, Leila Muresan, Bénédicte Sanson
            </div>
</div>
</div>
<div class="widget-dynamic-entry item at-widget-entry-SCL">
<span aria-hidden="true" class="hfDoi" data-attribute="10.1242/dev.202353"></span>
<div class="widget-dynamic-content-wrap">
<div class="widget-dynamic-journal-title">
<a href="/dev/article/doi/10.1242/dev.202353/346560/Mechanistic-regulation-of-planarian-shape-during">
                    Mechanistic regulation of planarian shape during growth and degrowth
                </a>
</div>
<div class="widget-dynamic-journal-authors">
                Jason M. Ko, Waverly Reginato, Andrew Wolff, Daniel Lobo
            </div>
</div>
</div>
</div>
<div class="widget-dynamic-browse">
<a href="//journals.biologists.com/dev/search-results?SearchSourceType=1%22*%22&amp;exPrm_qqq=%7b!payload_score+f%3dTags+func%3dmax%7d*&amp;q=*&amp;exPrm_fq=((JournalISSN%3a%220950-1991%22)+AND+(GroupTypes%3a%22JAM+Articles%22))&amp;hideSearchTerm=true">More accepted manuscripts</a>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="widget-DynamicWidgetLayout widget-instance-Issue_RightRailB0B2">
<div class="widget widget-dynamic issue-rssfeeds" data-count="1">
<div class="widget-dynamic-inner-wrap">
<div class="widget-RssFeeds widget-instance-Issue_RightRailB0B2Issue_Rss_Feeds">
<div class="widget vt-widget-rssfeeds widget-rssfeeds rail-widget_wrap" id="rssFeeds">
<h3 id="spRssFeedsTitle">RSS Feeds</h3>
<div class="widget-links_wrap">
<div><a href="https://journals.biologists.com/rss/site_1000005/1000005.xml">RSS Feed - Current Issue Only</a></div>
<div><a href="https://journals.biologists.com/rss/site_1000005/LatestOpenIssueArticles_1000005.xml">Open Issues RSS Feed</a></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="widget-DynamicWidgetLayout widget-instance-Issue_RightRailB0B3">
<div class="widget widget-dynamic issue-self-serve" data-count="1">
<div class="widget-dynamic-inner-wrap">
<div class="widget-SelfServeContent widget-instance-dev_issue-self-serve">
<input class="SelfServeContentId" type="hidden" value="issue-self-serve"/>
<input class="SelfServeVersionId" type="hidden" value="0"/>
<style>
    blockquote {
    margin: 1rem;
    font-size: 0.875em;
    }
</style>
<div class="rail-widget_wrap">
<h3><a href="https://bit.ly/48bHyLJ" target="_blank">Call for papers: Uncovering Developmental Diversity</a></h3>
<div class="widget-links_wrap">
<img alt="Banner with special issue title, guest editors and an image of a sea urchin" src="https://cob.silverchair-cdn.com/ImageLibrary/Development/Snippets/1223_Dev_CFP_Diversity.png?versionId=6662"/>
<p style="font-size: 0.875em;">Development invites you to submit your latest research to our <a href="https://bit.ly/48bHyLJ">upcoming special issue: Uncovering Developmental Diversity</a>. This issue will be coordinated by our academic Editor Cassandra Extavour (Harvard University, USA) alongside two Guest Editors: Liam Dolan (Gregor Mendel Institute of Molecular Plant Biology, Austria) and Karen Sears (University of California Los Angeles, USA).</p>
</div>
<hr style="width: 80%; margin-top: -5px;"/>
<h3><a href="https://bit.ly/3HS5tV6" target="_blank">Choose Development in 2024</a></h3>
<div class="widget-links_wrap">
<img alt='Head shot of James Briscoe and quote: "Where you choose to send your paper is not a neutral decision: publishing is poloitical. By choosing to send your next paper to Development you are demonstrating your support for a not-for-profit scientist-led journal, and you are signifying your commitment to the field and to the next generation of researchers."' src="https://cob.silverchair-cdn.com/ImageLibrary/Development/Snippets/0224_Dev_JamesBriscoe_Editorial.png?versionId=6662"/>
<p style="font-size: 0.875em;">In this <a href="https://bit.ly/3HS5tV6">Editorial</a>, Development Editor-in-Chief James Briscoe and Executive Editor Katherine Brown explain how you support your community by publishing in Development and how the journal champions serious science, community connections and progressive publishing.</p>
</div>
<hr style="width: 80%; margin-top: -5px;"/>
<h3><a href="https://bit.ly/42vUJVO" target="_blank">Journal Meeting: From Stem Cells to Human Development</a></h3>
<div class="widget-links_wrap">
<img alt="Promotional banner for Development 2024 Journal Meeting" src="https://cob.silverchair-cdn.com/ImageLibrary/Development/Snippets/0324_Dev_Meeting_Register_new.png?versionId=6662"/> 
<p style="font-size: 0.875em;">Register now for the 2024 Development Journal Meeting <a href="https://bit.ly/42vUJVO" target="_blank">From Stem Cells to Human Development</a>. Early-bird registration deadline: 3 May. Abstract submission deadline: 21 June.</p>
</div>
<hr style="width: 80%; margin-top: -5px;"/>
<h3><a href="https://bit.ly/3IxLbAh">Pluripotency of a founding field: rebranding developmental biology</a></h3>
<div class="widget-links_wrap">
<img alt="Selection of developmental biology images, incl. axolotl tadpole, drosophila ovaries, quail embryo and arabidopsis stem" src="https://cob.silverchair-cdn.com/ImageLibrary/Development/Snippets/0324_Dev_Perspective.png?versionId=6662"/>
<p style="font-size: 0.875em;">This collaborative <a href="https://bit.ly/3IxLbAh">Perspective</a>, the result of a workshop held in 2023, proposes a set of community actions to increase the visibility of the developmental biology field. The authors make recommendations for new funding streams, frameworks for collaborations and mechanisms by which members of the community can promote themselves and their research.</p>
</div>
<hr style="width: 80%; margin-top: -5px;"/>
<h3><a href="https://bit.ly/3NXfPp3" target="_blank">Read &amp; Publish Open Access publishing: what authors say</a></h3>
<div class="widget-links_wrap">
<img alt="" src="https://cob.silverchair-cdn.com/ImageLibrary/Development/Development%20Read%20and%20Publish.jpeg?versionId=6662"/>
<p style="font-size: 0.875em;">We have had great feedback from authors who have benefitted from our Read &amp; Publish agreement with their institution and have been able to publish Open Access with us without paying an APC.<a href="https://bit.ly/3NXfPp3" target="_blank"> Read what they had to say</a>.</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div><!-- /#Sidebar .page-column page-column-/-right issue-sidebar --> </div>
<div class="spinner"></div>
</div>
</div><!-- /.content-main_content -->
</section>
</div>
<div class="mobile-mask">
</div>
<section class="footer_wrap vt-site-footer">
<div class="ad-banner js-ad-banner ad-banner-footer">
<div class="widget-AdBlock widget-instance-FooterAd">
</div>
</div>
<div class="sticky-footer-ad js-sticky-footer-ad">
<div class="widget-AdBlock widget-instance-StickyAd">
</div>
</div>
<div class="widget-SitePageFooter widget-instance-SitePageFooter">
<div class="journal-footer journal-bg">
<div class="journal-footer_content clearfix foot-right">
<div class="journal-footer-menu">
<ul>
<li class="link-0">
<a href="/dev/pages/about">About Development</a>
</li>
<li class="link-1">
<a href="/dev/pages/edboard">Editors and Board</a>
</li>
<li class="link-2">
<a href="/dev/pages/aims">Aims and scope</a>
</li>
</ul>
<ul>
<li class="link-0">
<a href="/dev/pages/submit-manuscript">Submit a manuscript</a>
</li>
<li class="link-1">
<a href="/dev/pages/manuscript-prep">Manuscript preparation</a>
</li>
<li class="link-2">
<a href="/dev/pages/journal-policies">Journal policies</a>
</li>
</ul>
<ul>
<li class="link-0">
<a href="/dev/pages/rights-permissions">Rights and permissions</a>
</li>
<li class="link-1">
<a href="/dev/pages/alerts">Sign up for alerts</a>
</li>
<li class="link-2">
<a href="/dev/pages/contacts">Contacts</a>
</li>
</ul>
</div>
<div class="journal-footer-affiliations aff-right">
<!-- <h3>Affiliations</h3> -->
<a href="/dev" target="">
<img alt="Development" class="journal-footer-affiliations-logo" id="footer-logo-Development" src="//cob.silverchair-cdn.com/data/SiteBuilderAssets/Live/Images/dev/DEV_footer127823882.svg"/>
</a>
</div>
</div>
</div>
</div>
<div class="site-theme-footer">
<div class="site-theme-footer_content">
<div class="widget-SelfServeContent widget-instance-UmbrellaFooterSelfServe">
<input class="SelfServeContentId" type="hidden" value="GlobalFooter_Links"/>
<input class="SelfServeVersionId" type="hidden" value="0"/>
<div class="theme-footer">
<div class="flex-row">
<div class="col-6 footer-nav">
<div class="flex-row">
<div class="col-2">
<div class="footer-links-group with-header">
<ul class="list-lvl-0 long-links">
<li class="list-lvl-0"><a href="/dev" target="_blank">Development</a></li>
<li class="list-lvl-0"><a href="/jcs" target="_blank">Journal of Cell Science</a></li>
<li class="list-lvl-0"><a href="/jeb" target="_blank">Journal of Experimental Biology</a></li>
<li class="list-lvl-0"><a href="/dmm" target="_blank">Disease Models &amp; Mechanisms</a></li>
<li class="list-lvl-0"><a href="/bio" target="_blank">Biology Open</a></li>
</ul>
</div>
</div>
<!-- close .col-2-->
<div class="col-2">
<div class="footer-links-group">
<ul class="list-lvl-0">
<li class="list-lvl-0"><a href="https://thenode.biologists.com/">The Node</a></li>
<li class="list-lvl-0"><a href="https://prelights.biologists.com/">preLights</a></li>
<li class="list-lvl-0"><a href="https://focalplane.biologists.com/">FocalPlane</a></li>
</ul>
</div>
</div>
<!-- close .col-2-->
<div class="col-2">
<div class="footer-links-group">
<ul class="list-lvl-0">
<li class="list-lvl-0"><a href="https://www.biologists.com/grants">Grants</a></li>
<li class="list-lvl-0"><a href="https://www.biologists.com/meetings">Journal Meetings</a></li>
<li class="list-lvl-0"><a href="https://www.biologists.com/workshops">Workshops</a></li>
</ul>
</div>
</div>
<!-- close .col-2-->
<div class="col-2">
<div class="footer-links-group">
<ul class="list-lvl-0">
<li class="list-lvl-0"><a href="https://www.biologists.com/library-hub">Library hub</a></li>
<li class="list-lvl-0"><a href="https://www.biologists.com/subscribe">Company news</a></li>
<li class="list-lvl-0"><a href="https://www.biologists.com/contact">Contacts</a></li>
</ul>
</div>
</div>
<!-- close .col-2-->
</div>
<!-- close .footer-nav .flex-row -->
</div>
<!-- close .footer-nav -->
<div class="col-3 footer-branding">
<div class="footer-logo-wrap">
<!-- If there are multiple logos, duplicate div.footer-logo -->
<div class="footer-logo">
<a href="/journals">
<img alt="The Company of Biologists Logo" src="https://cob.silverchair-cdn.com/ImageLibrary/logo-footer.svg?versionId=6231"/>
</a>
</div>
</div>
<div class="social-icons-wrap">
<ul class="social-icons-list"><a href="#">
<!-- Twitter -->
</a>
<li><a href="#"></a><a class="social-link" href="https://twitter.com/Co_Biologists"><span class="icon-social-twitter"></span><span class="screenreader-text">Twitter</span></a></li>
<!-- LinkedIn -->
<li><a class="social-link" href="https://www.linkedin.com/company/the-company-of-biologists/"><span class="icon-social-linkedin"></span><span class="screenreader-text">LinkedIn</span></a></li>
<!--Youtube---->
<li><a class="social-link" href="https://www.youtube.com/user/CompanyofBiologists"><span class="icon-social-youtube"></span><span class="screenreader-text">Youtube</span></a></li>
<!-- WeChat-->
<li><a class="social-link social-link-wechat" href="/ImageLibrary/WeChat.jpg" target="_blank"><span><img alt="WeChat logo" src="https://cob.silverchair-cdn.com/ImageLibrary/wechat-white-transparent-noring.png?versionId=3065" style="height: 22px;margin-top: 9px;"/>
<style>
        .social-link-wechat:hover, .social-link-wechat:focus {
        color:transparent !important;
        }
        .social-link-wechat:hover img, .social-link-wechat:focus img {
        filter: invert(100);
        }
    </style>
</span></a></li>
<!-- Mastodon-->
<li><a class="social-link social-link-mastodon" href="https://biologists.social/@Co_Biologists" target="_blank"><img alt="Mastodon icon" src="https://cob.silverchair-cdn.com/ImageLibrary/Mastodon_Social_Icon_Circle_BW_TransparencyNoBlk.png?versionId=6231" style="width: 38px; height: 38px; margin-top: 0px;"/><br/>
</a></li>
</ul>
</div>
</div>
<!-- close .footer-branding -->
</div>
<!-- close .flex-row -->
</div>
<!-- close .theme-footer -->
<div class="legal-links-row">
<div class="legal-links-wrap">
<ul class="legal-links">
<li><a href="https://www.biologists.com/privacy-policy">Privacy policy</a></li>
<li><a href="https://www.biologists.com/terms-conditions">Terms &amp; conditions</a></li>
<li><a href="https://www.biologists.com/copyright-permissions">Copyright policy</a></li>
<li><a href="https://www.biologists.com/cookies/">Cookies</a></li>
<li class="copyright">© 2024 The Company of Biologists. All rights reserved.</li>
</ul>
<ul class="legal-links">
<li>Registered Charity 277992 | Registered in England and Wales | Company Limited by Guarantee No 514735<br/>
    Registered office: Bidder Building, Station Road, Histon, Cambridge CB24 9LF, UK</li>
</ul>
</div>
<!-- close .legal-links-wrap -->
</div>
<!-- close .legal-links-row -->
</div>
</div><!-- /.center-inner-row -->
</div><!-- /.site-theme-footer -->
<div class="ss-ui-only">
<div class="widget-SelfServeContent widget-instance-SSuiOnlySelfServe">
<input class="SelfServeContentId" type="hidden" value="SSuiOnly"/>
<input class="SelfServeVersionId" type="hidden" value="0"/>
<style type="text/css">
    .boxed-text .caption {
    display: block;
    }
    .boxed-text .caption .title.-title {
    float: none;
    font-weight: bold;
    margin-bottom: .75rem;
    }
    /* Start COB-414 */
    .base-font {
    font-size: 1rem !important;
    }
    .widget-SitePageFooter .journal-footer .journal-footer_content {
    flex-wrap: nowrap !important;
    }
    @media (max-width: 899px) {
    .widget-SitePageFooter .journal-footer .journal-footer_content {
    flex-wrap: wrap !important;
    }
    }
    .site-theme-footer .site-theme-footer_content .legal-links-row {
    background: #646262;
    padding: 1rem 0;
    }
    .site-theme-footer .site-theme-footer_content .legal-links-row .legal-links-wrap {
    float: none;
    max-width: 1300px;
    margin: 0 auto;
    padding: 0 1rem;
    }
    /* End COB-414 */
    /* Start COB-415 */
    .article-title-main {
    font-size: 1.75rem !important;
    }
    .pg_article h4.section-title {
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: .5px !important;
    }
    .pg_article .content-inner-wrap h2 {
    font-size: 1.375rem !important;
    }
    .pg_article .content-inner-wrap h4 {
    font-size: 0.875rem !important;
    }
    /* End COB-415 */
    /*SCMP-26926*/
    body.leftRailModalOpen .page-column--center.can-stick {
    z-index: 1;
    }
    /*SCMP-26926*/
    /*Self Serve overrides*/
    .widget-SelfServeContent .homepage-panel-text h1,
    .widget-SelfServeContent .homepage-panel-text h2,
    .widget-SelfServeContent .homepage-panel-text h3,
    .widget-SelfServeContent .homepage-panel-text h4 {
    margin-top: 0;
    }
    .widget-SelfServeContent .homepage-panel-text h1+p,
    .widget-SelfServeContent .homepage-panel-text h2+p,
    .widget-SelfServeContent .homepage-panel-text h3+p,
    .widget-SelfServeContent .homepage-panel-text h4+p {
    margin-top: .25rem;
    }
    .widget-SelfServeContent h1+p,
    .widget-SelfServeContent h2+p,
    .widget-SelfServeContent h3+p,
    .widget-SelfServeContent h4+p {
    margin-top: .25rem;
    }
    .widget-SelfServeContent h1,
    .widget-SelfServeContent h2,
    .widget-SelfServeContent h3,
    .widget-SelfServeContent h4 {
    margin-top: 1rem;
    }
    .widget-SelfServeContent h1+h2,
    .widget-SelfServeContent h2+h3,
    .widget-SelfServeContent h3+h4 {
    margin-top: .5rem;
    }
    .widget-SelfServeContent h1 {
    font-size: 1.75rem;
    }
    .widget-SelfServeContent h2 {
    font-size: 1.4rem;
    }
    .widget-SelfServeContent h3 {
    font-size: 1.25rem;
    }
    .widget-SelfServeContent h4 {
    font-size: 1.125rem;
    }
    .widget-SelfServeContent h5 {
    font-size: 16px;
    font-weight: bold;
    }
    .widget-SelfServeContent p+ul,
    .widget-SelfServeContent p+ol {
    margin-top: -.75rem;
    margin-bottom: .75rem;
    }
    /*end self serve overrides*/
    .pg_Collections .widget-MultiQuerySelectableContentList {
    border: none;
    }
</style>
</div>
</div>
<div class="ad-banner js-ad-interstitial">
<div class="widget-AdBlock widget-instance-Interstitial">
</div>
</div>
</section>
<div class="widget-SiteWideModals widget-instance-SiteWideModals">
<div class="reveal-modal" data-reveal="" id="revealModal">
<div id="revealContent"></div>
<a class="close-reveal-modal" href="javascript:;"><i class="icon-general-close"><span class="screenreader-text">Close Modal</span></i></a>
</div>
<div class="modal-global-container" id="globalModalContainer">
<div id="globalModalContent">
<div class="js-globalModalPlaceholder"></div>
</div>
<a class="close-modal js-close-modal" href="javascript:;"><i class="icon-general-close"><span class="screenreader-text">Close Modal</span></i></a>
</div>
<div class="modal-overlay js-modal-overlay" id="globalModalOverlay"></div>
<div class="reveal-modal small" data-reveal="" id="NeedSubscription">
<div class="subscription-needed">
<h5 class="modal-heading">This Feature Is Available To Subscribers Only</h5>
<p><a class="btn modal-sign_in-btn" href="/sign-in?returnUrl=%2fdev%2fissue%2f151%2f7">Sign In</a> or <a class="modal-register-link" href="/my-account/register?siteId=1000005&amp;returnUrl=%2fdev%2fissue%2f151%2f7">Create an Account</a></p>
</div>
<a class="close-reveal-modal" href="javascript:;"><i class="icon-general-close"><span class="screenreader-text">Close Modal</span></i></a>
</div>
<div class="reveal-modal tiny" data-reveal="" id="noAccessReveal">
<a class="close-reveal-modal" href="javascript:;"><i class="icon-general-close"><span class="screenreader-text">Close Modal</span></i></a>
<div id="noAccessForm">
<div class="spinner"></div>
</div>
</div>
</div>
<script type="text/javascript">
    MathJax = {
        tex: {
            inlineMath: [['|$', '$|'], ['\\(', '\\)']]
        }
    };
</script>
<script async="" id="MathJax-script" src="//cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!-- CookiePro Default Categories -->
<!-- When the Cookie Compliance code loads, if cookies for the associated group have consent...
         it will dynamically change the tag to: script type=text/JavaScript...
         the code inside the tags will then be recognized and run as normal. -->
<script src="//cob.silverchair-cdn.com/Themes/Client/app/jsdist/v-638488182993945370/site.min.js" type="text/javascript"></script>
<script type="text/javascript">
        $(document).ready(function () {
            App.SearchAutoComplete.init(["Keywords"]);
        });
        </script>
<div class="ad-banner js-ad-riser ad-banner-riser">
<div class="widget-AdBlock widget-instance-RiserAd">
</div>
</div>
<div class="end-of-page-js"></div>
</body>
</html>


"""

soup = BeautifulSoup(html, 'html.parser')

# Find all <a> elements with the specified class
link = soup.find('a', class_='al-link pdf openInAnotherWindow stats-item-pdf-download js-download-file-gtm-datalayer-event article-pdfLink').get('href')
modified_url = "https://journals.biologists.com" + link
print(modified_url)