(function($) {
    $(document).ready(function() {
        $(document.body).on('click', '.product-view.product-grid-lg', function() {
            $('.grid.product-grid').removeClass('grid--3-col-desktop').addClass('grid--4-col-desktop');
            $('.product-view.product-grid-lg').addClass('active');
            $('.product-view.product-grid').removeClass('active');
        });

        $(document.body).on('click', '.product-view.product-grid', function() {
            $('.grid.product-grid').removeClass('grid--4-col-desktop').addClass('grid--3-col-desktop');
            $('.product-view.product-grid').addClass('active');
            $('.product-view.product-grid-lg').removeClass('active');
        });
    });
})(jQuery);
