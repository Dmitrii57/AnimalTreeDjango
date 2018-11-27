from django.db import models
from itertools import chain
from species.models.kingdoms import Kingdoms

class Species(models.Model):
    id = models.BigAutoField(primary_key=True)
    kingdom = models.ForeignKey(Kingdoms, models.DO_NOTHING)
    title = models.TextField()
    page_url = models.TextField()
    type = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = 'species'
        managed = False
        db_table = 'list'
        unique_together = (('kingdom', 'title'),)

    def init_childs(self):
        self.childs = Species.objects.filter(parent=self.id)
        return self.childs

    def init_childs(self, t):
        self.childs = Species.objects.filter(parent=self.id).exclude(id = t.id)
        self.childs = list(chain(self.childs, [t]))
        return self

    def init_tree_structure(self, depth):
        if (depth):
            depth -= 1
            cur_childs = self.init_childs()
            for child in cur_childs:
                child.init_tree_structure(depth)

    def get_root(self):
        cur = self
        while(cur.parent != None):
            cur = Species.objects.get(id=cur.parent.id).init_childs(cur)
        return cur