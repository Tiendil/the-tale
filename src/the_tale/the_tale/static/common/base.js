
if (!window.pgf) {
    pgf = {};
}

if (!pgf.base) {
    pgf.base = {};
}

if (typeof(Storage)!=="undefined") {
    pgf.base.settings = {
        _prefix: undefined,
        init: function(prefix) {
            this._prefix = prefix;
        },
        set: function(key, value) {
            localStorage[this._prefix+'_'+key] = value;
        },
        get: function(key, def) {
            key = this._prefix+'_'+key;
            if (!(key in localStorage)) return def;
            return localStorage[key];
        }
    };
}
else {
    pgf.base.settings = {
        init: function(prefix) {},
        set: function(key, value) {},
        get: function(key, def) {return def;}
    };
}


pgf.base.ToggleWait = function(element, wait) {
    element.spin(wait ? 'tiny' : false);
    element.toggleClass('wait', wait).toggleClass('pgf-wait', wait);
};

pgf.base.InitializeTabs = function(settingName, def, tabs) {

    var tabShowed = false;

    var openTab = pgf.base.settings.get(settingName, def);

    function SetHash(id) {
        window.location.hash = '#'+settingName+'='+id;
    }

    for (var i in tabs) {
        var id = tabs[i][1];
        if (window.location.hash.indexOf(settingName+'='+id) != -1) {
            openTab = id;
            break;
        }
    }

    for (var i in tabs) {
        var selector = jQuery(tabs[i][0]);

        if (selector.length == 0) {
            continue;
        }

        var id = tabs[i][1];

        if (openTab == id) {
            selector.tab('show');
            SetHash(id);
            tabShowed = true;
        }

        (function(id) {
            selector.click(function(e) {
                pgf.base.settings.set(settingName, id);
                SetHash(id);
            });
        })(id);
    }

    if (!tabShowed) {
        for (var i in tabs) {
            var selector = jQuery(tabs[i][0]);
            var id = tabs[i][1];

            if (selector.length) {
                selector.tab('show');
                SetHash(id);
                break;
            }
        }
    }

    jQuery(window).bind('hashchange', function() {
        for (var i in tabs) {
            var selector = jQuery(tabs[i][0]);
            var id = tabs[i][1];
            if (window.location.hash.indexOf(settingName+'='+id) != -1) {
                selector.tab('show');
                break;
            }
        }
    });
};

pgf.base.TOOLTIP_WIDTH = 400;

pgf.base.TooltipPlacement = function (tip, element) {
    element = jQuery(element);

    var offset = element.offset();
    var placement = element.data('tooltip-placement');

    // if owner was deleted
    if (offset.left == 0 && offset.top == 0) {
        jQuery(tip).addClass('pgf-hidden');
    }

    if (!placement) {
        var height = Math.min(jQuery(document).outerHeight(), jQuery(window).height());
        var width = Math.min(jQuery(document).outerWidth(), jQuery(window).width());
        var vert = 0.5 * height - offset.top;
        var vertPlacement = vert > 0 ? 'bottom' : 'top';
        var horiz = 0.5 * width - offset.left;
        var horizPlacement = horiz > 0 ? 'right' : 'left';
        placement = Math.abs(horiz) > Math.abs(vert) ?  horizPlacement : vertPlacement;
    }
    return placement;
};

pgf.base.HorizTooltipPlacement = function (tip, element) {
    element = jQuery(element);

    var offset = element.offset();
    var placement = element.data('tooltip-placement');

    // if owner was deleted
    if (offset.left == 0 && offset.top == 0) {
        jQuery(tip).addClass('pgf-hidden');
    }

    if (!placement) {
        var width = jQuery(document).outerWidth();
        var horiz = 0.5 * width - offset.left;
        var horizPlacement = horiz > 0 ? 'right' : 'left';
        placement = horizPlacement;
    }
    return placement;
};

pgf.base.tooltipsArgs = { animation: true,
                          placement: pgf.base.TooltipPlacement,
                          delay: { show: 500,
                                   hide: 100 } };

pgf.base.popoverArgs = { animation: true,
                         placement: pgf.base.TooltipPlacement,
                         delay: { show: 500,
                                  hide: 100 } };

pgf.base._FindParentsForChildren = function(parent, child) {
    if (child) return jQuery('.'+parent+' .'+child).closest('.'+parent);
    return jQuery('.'+parent);
};

pgf.base.HideTooltips = function(clearedContainer, child_class) {
    pgf.base._FindParentsForChildren('popover', child_class).remove();
    pgf.base._FindParentsForChildren('tooltip', child_class).remove();

    if (clearedContainer) {
        // TODO: data('x').enabled = false — totally disabled toltips, we need other way to hide them
        // TODO: is first processing needed????
        jQuery('.pgf-has-popover', clearedContainer).each(function(i, el){
                                                              el = jQuery(el);
                                                              el.data('popover').enabled = false;
                                                          });
        jQuery('[rel="popover"]', clearedContainer).each(function(i, el){
                                                             el = jQuery(el);
                                                             el.data('popover').enabled = false;
                                                         });
        jQuery('[rel="tooltip"]', clearedContainer).each(function(i, el){
            el = jQuery(el);
            tooltipObject = el.data('tooltip');
            if (tooltipObject) {
                tooltipObject.enabled = false;
            }
        });
        if (clearedContainer.data('tooltip')) clearedContainer.data('tooltip').enabled = false;
        if (clearedContainer.data('popover')) clearedContainer.data('tooltip').enabled = false;
    }
};

pgf.base.RenderTemplateList = function(selector, data, newElementCallback, params) {

    var container = jQuery(selector);
    var template = jQuery('.pgf-template', container).eq(0);

    container.children().not('.pgf-template').not('.pgf-empty-template').remove();

    for (var i in data) {
        var elementData = data[i];

        var newElement = template
            .clone(false, false)
            .appendTo(container)
            .removeClass('pgf-template');

        newElement.addClass(i % 2 ? 'even' : 'odd');

        if (newElementCallback) {
            newElementCallback(i, elementData, newElement);
        }
    }
};

function _PrependZero(text) {
    return ('0' + text).slice(-2);
}

pgf.base.AutoFormatTime = function() {
    var date = new Date();

    jQuery('.pgf-format-datetime').each(function(i, v){
        var el = jQuery(v);
        var timestamp = parseInt(el.data('timestamp'), 10) * 1000;
        var date = new Date(timestamp)
        var text = _PrependZero(date.getDate()) + '.' + _PrependZero(date.getMonth()+1) + '.' + date.getFullYear() + ' ' + _PrependZero(date.getHours()) + ':' + _PrependZero(date.getMinutes());
        el.text(text);
    });

    jQuery('.pgf-format-date').each(function(i, v){
        var el = jQuery(v);
        var timestamp = parseInt(el.data('timestamp'), 10) * 1000;
        var date = new Date(timestamp)
        var text = _PrependZero(date.getDate()) + '.' + _PrependZero(date.getMonth()+1) + '.' + date.getFullYear();
        el.text(text);
    });

    jQuery('.pgf-format-time').each(function(i, v){
        var el = jQuery(v);
        var timestamp = parseInt(el.data('timestamp'), 10) * 1000;
        var date = new Date(timestamp)
        var text = _PrependZero(date.getHours()) + ':' + _PrependZero(date.getMinutes());
        el.text(text);
    });
};

pgf.base.FormatTimeDelta = function(delta) {
    var hours = parseInt(Math.floor(delta / (60*60)));
    var minutes = parseInt(Math.floor((delta-hours*60*60) / 60))
    var seconds = parseInt(Math.floor((delta-hours*60*60-minutes*60)));

    var result = '';

    if (hours>0) {
        result += hours + ':'
    }

    result += ('0' + minutes).slice(-2) + ':' + ('0' + seconds).slice(-2);

    return result;
}

pgf.base.AddPreview = function(blockSelector, contentSourceSelector, previewUrl) {

    var block = jQuery(blockSelector);
    var source = jQuery(contentSourceSelector, block);

    var previewButton = jQuery('.pgf-preview-button', block);
    var editButton = jQuery('.pgf-edit-button', block);
    var editContent = jQuery('.pgf-edit-content', block);
    var previewContent = jQuery('.pgf-preview-content', block);

    function SwitchView(preview) {
        previewButton.toggleClass('pgf-hidden', preview);
        editContent.toggleClass('pgf-hidden', preview);
        editButton.toggleClass('pgf-hidden', !preview);
        previewContent.toggleClass('pgf-hidden', !preview);
    }

    previewButton.click(function(e){
        jQuery.ajax({type: 'post',
                     data: { text: source.val() },
                     url: previewUrl,
                     success: function(data) {
                         previewContent.html(data);
                         SwitchView(true);
                     }
                    });
    });

    editButton.click(function(e){
        SwitchView(false);
    });
};


pgf.base.InitBBFields = function(containerSelector) {
    var container = jQuery(containerSelector);
    jQuery('.pgf-bb-command', container).click(function(e){
        e.preventDefault();

        var target = jQuery(e.currentTarget);

        var content = jQuery('textarea', target.parents('.pgf-widget'));

        var text = content.val();

        var textarea = content.get(0);

        var selectionStart = textarea.selectionStart;
        var selectionEnd = textarea.selectionEnd;

        var tagName = target.data('tag');

        var single = target.data('single');

        if (single) {
            text = text.substring(0, selectionStart) +
                '[' + tagName + ']' + text.substring(selectionStart, selectionEnd) +
                text.substring(selectionEnd, text.length);
        }
        else {
            text = text.substring(0, selectionStart) +
                '[' + tagName + ']' + text.substring(selectionStart, selectionEnd) + '[/' + tagName + ']' +
                text.substring(selectionEnd, text.length);
        }

        content.val(text);

    });
};

pgf.base.CompareObjects = function(a, b)
{
  if (a == undefined && b != undefined) return false;
  if (b == undefined && a != undefined) return false;

  var p;
  for(p in a) {
      if(typeof(b[p])=='undefined') {return false;}
  }

  for(p in a) {
      if (a[p]) {
          switch(typeof(a[p])) {
              case 'object':
                  if (!pgf.base.CompareObjects(a[p],b[p])) { return false; } break;
              case 'function':
                  if (typeof(b[p])=='undefined' ||
                      (a[p].toString() != b[p].toString()))
                      return false;
                  break;
              default:
                  if (a[p] != b[p]) { return false; }
          }
      } else {
          if (b[p])
              return false;
      }
  }

  for(p in b) {
      if(typeof(a[p])=='undefined') {return false;}
  }

  return true;
};


// convert subset of html into bbcode
pgf.base.HTMLToBBcode = function(text) {

    text = text
        .replace(/<strong>/g, '[b]')
        .replace(/<\/strong>/g, '[/b]')

        .replace(/<em>/g, '[i]')
        .replace(/<\/em>/g, '[/i]')

        .replace(/<u>/g, '[u]')
        .replace(/<\/u>/g, '[/u]')

        .replace(/<strike>/g, '[s]')
        .replace(/<\/strike>/g, '[/s]')

        .replace(/<blockquote>/g, '[quote]')
        .replace(/<\/blockquote>/g, '[/quote]')

        .replace(/<ul>/g, '[list]')
        .replace(/<\/ul>/g, '[/list]')

        .replace(/<li>/g, '[*]')
        .replace(/<\/li>/g, '')

        .replace(/<img src="([^"]*)">/g, '[img]$1[/img]')
        .replace(/<\/img>/g, '')

        .replace(/<a[^>]*href="([^"]*)"[^>]*>/g, '[url=$1]')
        .replace(/<\/a>/g, '[/url]')

        .replace(/\s+/g, ' ')

        .replace(/<br>/g, '\r')
        .replace(/<hr>/g, '[hr]')

        .replace(/<p>/g, '\r\r')
        .replace(/<\/p>/g, '')

        .replace(/&nbsp;/g, ' ');

    // replace spolers
    text = text
        .replace(/\[url=#pgf-spoiler-element-[\w\d]+\]([^\]]*)\[\/url\]/g, "[spoiler=$1]\r")
        .replace(/<\s*div\s*class="accordion-heading"\s*>([^<]*)<\/div>/g, "$1")
        .replace(/<\s*div\s*class="accordion-inner"\s*>([^<]*)<\/div>/g, "$1")
        .replace(/<\s*div[^>]+pgf-spoiler[^>]+>([^<]*)<\/div>/g, "$1")
        .replace(/<\s*div\s*class="accordion-group"\s*>([^<]*)<\/div>/g, "$1")
        .replace(/<\s*div[^>]+class="accordion"[^>]+>([^<]*)<\/div>/g, "$1\r[/spoiler]");

    // replace any other html elements

    text = text
        .replace(/<[^>]*>/g, "")
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>');

    return text;
};


pgf.base.OpenFancybox = function(images) {
          jQuery.fancybox.open(images, {  padding: 0,
                                          nextClick: true,
                                          openEffect: "fade",
                                          closeEffect: "fade",
                                          nextEffect: "fade",
                                          prevEffect: "fade",
                                          openSpeed: 500,
                                          closeSpeed: 500,
                                          nextSpeed: 500,
                                          prevSpeed: 500});
};

pgf.base.OpenFancyboxIntroComix = function(staticContent) {
    var images = [];

    if (staticContent.indexOf('http:') == -1) {
        staticContent = 'http:'+staticContent;
    }

    for (var i=0; i < 24; ++i) {
        var name = i < 10 ? '0'+i : i;
        images.push({href : staticContent + "images/intro_comix/"+name+".gif"});
    }

    pgf.base.OpenFancybox(images);
};


pgf.base.UpdateElementTooltip = function(element, tooltip, tooltipClass, tooltipsArgs) {
    if (element.data('current-tooltip') != tooltip) {
        pgf.base.HideTooltips(element, tooltipClass);
        element.data('current-tooltip', tooltip);
        if (element.data('tooltip')) {
            element.data('tooltip').options.title = tooltip;
            element.data('tooltip').enabled = true;
        }
        else {
            element.tooltip(jQuery.extend(true, {}, tooltipsArgs, {title: tooltip}));
        }
    }
};


pgf.base.RandomItem = function(array) {
    return array[Math.floor(Math.random() * array.length)];
}
