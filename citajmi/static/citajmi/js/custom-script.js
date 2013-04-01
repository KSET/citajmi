// /* Large desktop */
// @media (min-width: 1200px) { ... }
// /* Portrait tablet to landscape and desktop */
// @media (min-width: 768px) and (max-width: 979px) { ... }
// /* Landscape phone to portrait tablet */
// @media (max-width: 767px) { ... }
// /* Landscape phones and down */
// @media (max-width: 480px) { ... }
function init_masonry() {
    var $container = $('#masonry');
    var gutter = 16;
    var min_width = 254;    // minimum column width (in example it is 150px)
    $container.imagesLoaded(function() {
        $container.masonry({
            itemSelector : '.box',
            gutterWidth: gutter,
            isAnimated: true,
            columnWidth: function(containerWidth) {
                var num_of_boxes = (containerWidth/min_width | 0);
                var box_width = (((containerWidth - (num_of_boxes-1)*gutter)/num_of_boxes) | 0);
                if (containerWidth < min_width) {
                    box_width = containerWidth;
                }
                $('.box').width(box_width);
                return box_width;
            }
        });
    });
}
function resize_masonry() {
    $('#masonry').resize();
}
function init_masonry_filter() {
    $('#masonry-filter a').click(function() {
        // set active link
        $('#masonry-filter li').removeClass('active');
        $(this).parent().addClass('active');
        // hide show list items
        var filter = $(this).attr('href').substring(1);
        $('#masonry #box_list li:not(.'+filter+')').hide();
        $('#masonry #box_list li.'+filter).show();
        resize_masonry();
        return false;
    });
}
$(document).ready(function() {
    init_masonry();
    init_masonry_filter();
    setTimeout(resize_masonry, 500); // .5 sec, to fix padding
});
