(function($) {
    $(function() {
        console.log('your message');
        console.log('HIII');
        alert('hi')

        var selectField = $('#id_Activite'),
            verified = $('#id_AutreActivite');

        function toggleVerified(value) {
            value == 'Actif' ? verified.show() : verified.hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);