from django.test import TestCase
from lists.models import Item
from django.test import LiveServerTestCase
# Create your tests here.

class HomePageTest(LiveServerTestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/home/')
    #     self.assertEqual(found.func,home_page)

    #第一种创建请求的方式
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf-8')
    #     print(f"html:{html}")
    #     self.assertTrue(html.startswith('<!DOCTYPE html>'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.endswith('d'))

    # 第二种创建请求的方式
    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/home/')
    #     html = response.content.decode('utf-8')
    #     self.assertTrue(html.startswith('<!DOCTYPE html>'))
    #     self.assertTemplateUsed(response,'home.html')

    # def test_uses_home_template(self):
    #     response = self.client.get('/home/')
    #     self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/home/',data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/home/',data={'item_text':'A new list item'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(),0)

    def test_display_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/home/')

        self.assertIn('itemey 1',response.content.decode())
        self.assertIn('itemey 2',response.content.decode())


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)
        fist_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(fist_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'Item the second')




