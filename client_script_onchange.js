// ServiceNow Client Script | Type: onChange | Table: Incident | Field: Category
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
    if (isLoading || newValue == '') return;
    if (newValue == 'software') g_form.setValue('priority','2');
    else if (newValue == 'hardware') g_form.setValue('priority','3');
}
