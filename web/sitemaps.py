from django.contrib.sitemaps import Sitemap
from scrape.models import CountryTable, CityTable, StateTable

class CountrySitemap(Sitemap):
    def items(self):
        return CountryTable.objects.all()
    def location(self, obj):
        return f"/cost/{obj.Name}"
    
    def lastmod(self, obj):
        # Replace 'updated_at' with the actual field representing the last modified date in the CityTable model
        pass




class CitySitemap(Sitemap):

    def items(self):
        return CityTable.objects.all()
    
    def location(self, obj):
        if obj.state_name == '-':
            return f"/cost/{obj.country_name}/{obj.Name}"
        else:
            return f"/cost/{obj.country_name}/{obj.state_name}/{obj.Name}"




class StateSitemap(Sitemap):

    def items(self):
        return StateTable.objects.all()
    
    def location(self, obj):
        return f"/cost/{obj.country_name}/{obj.Name}"


class BestCountrySitemap(Sitemap):
    def items(self):
        return CountryTable.objects.all()
    def location(self, obj):
        return f"/best/{obj.Name}"
    
    def lastmod(self, obj):
        # Replace 'updated_at' with the actual field representing the last modified date in the CityTable model
        pass




class BestCitySitemap(Sitemap):

    def items(self):
        return CityTable.objects.all()
    
    def location(self, obj):
        if obj.state_name == '-':
            return f"/best/{obj.country_name}/{obj.Name}"
        else:
            return f"/best/{obj.country_name}/{obj.state_name}/{obj.Name}"




class BestStateSitemap(Sitemap):

    def items(self):
        return StateTable.objects.all()
    
    def location(self, obj):
        return f"/best/{obj.country_name}/{obj.Name}"
