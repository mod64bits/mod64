from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.http import require_POST



class BaseViews:
    def __init__(self, model=None, form_class=None,  listChanged=None ):
        self.model = model
        self.form_class = form_class
        self.listChanged = listChanged


    @staticmethod
    def index_view(request, template_name):
        return render(request, template_name=template_name)

    def list_view(self, request, template_name):
        return render(request, template_name, {'object_list': self.model.objects.all().order_by('-created')})

    def add_view(self, request, template_name):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                form_obj = form.save()
                return HttpResponse(
                    status=204,
                    headers={
                        'HX-Trigger': json.dumps({
                            self.listChanged: None,
                            "showMessage": f"{form_obj.nome} Adcionado."
                        })
                    })
        else:
            form = self.form_class()
        return render(request, template_name, {
            'form': form,
        })

    def edit_view(self, request, pk, template_name):
        obj_model = get_object_or_404(self.model, pk=pk)
        if request.method == "POST":
            form = self.form_class(request.POST, instance=obj_model)
            if form.is_valid():
                form.save()
                return HttpResponse(
                    status=204,
                    headers={
                        'HX-Trigger': json.dumps({
                            self.listChanged: None,
                            "showMessage": f"{obj_model.nome} Atuializado."
                        })
                    }
                )
        else:
            form = self.form_class(instance=obj_model)
        return render(request, template_name, {
            'form': form,
            'obj_model': obj_model,
        })


    def delete_view(self, request, pk):
        obj_model = get_object_or_404(self.model, pk=pk)
        obj_model.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    self.listChanged: None,
                    "showMessage": f"{obj_model.nome} deletado."
                })
            })

def addBaseView(request, form, template):

    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            form_obj = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "fornecedorListChanged": None,
                        "showMessage": f"{form_obj.nome} Adcionado."
                    })
                })
    else:
        form = form()
    return render(request, template, {
        'form': form,
    })

def editBaseView(request, pk, model, form, template):
    obj_model = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = form(request.POST, instance=obj_model)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "fornecedorListChanged": None,
                        "showMessage": f"{obj_model.nome} Atuializado."
                    })
                }
            )
    else:
        form = form(instance=obj_model)
    return render(request, template, {
        'form': form,
        'obj_model': obj_model,
    })

