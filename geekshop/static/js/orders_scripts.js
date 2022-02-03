window.onload = function () {
    TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

    var quantities = [];
    var prices = [];
    var orderitem_num, delta_quantity, orderitem_quantity, delta_cost;

    var order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for(var i=0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));

        quantities[i] = _quantity; 
        if (_price) {
            prices[i] = _price; } 
        else {
            prices[i] = 0; 
        }
    }

    if (!order_total_quantity) {
        for (var i=0; i < TOTAL_FORMS; i++) {
            order_total_quantity += quantities[i]
            order_total_cost += quantities[i] * prices[i]
        }

        $('.order_total_cost').text(order_total_cost)
        $('.order_total_quantity').text(order_total_quantity)
    }

    $('.order_form').on('click', 'input[type="number"]', function (event) {
        var target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));

        if (prices[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantities[orderitem_num]; 
            quantities[orderitem_num] = orderitem_quantity; 
            orderSummaryUpdate(prices[orderitem_num], delta_quantity);
        } 
    });

    $('.formset_row').formset({
        addText: 'добавить продукт', 
        deleteText: 'удалить', 
        prefix: 'orderitems', 
        removed: deleteOrderItem
        });

    function deleteOrderItem(row) {
        var target_name= row[0].querySelector('input[type="number"]').name; 
        orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', '')); 
        delta_quantity = -quantities[orderitem_num];
        orderSummaryUpdate(prices[orderitem_num], delta_quantity); }

    
    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;
    
        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2)); 
        order_total_quantity = order_total_quantity + delta_quantity;
        
        $('.order_total_cost').html(order_total_cost.toString());
        $('.order_total_quantity').html(order_total_quantity.toString()); 
    }

}




     

