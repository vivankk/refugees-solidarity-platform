import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class BlogService {
  private base_url = 'http://localhost:5000/'
  private add_blog_url = this.base_url + 'add_blog';
  private get_all_blogs_url = this.base_url + 'messages';
  private delete_blog_url = this.base_url + 'delete_message/';
  private get_single_blog_url = this.base_url + 'message/';
  private update_blog_url = this.base_url + 'update_blog/';

  constructor(private http: HttpClient) { }

  add_blog(blogProps: Object) {
    return this.http.post(this.add_blog_url, blogProps);
  }

  get_all_blogs() {
      return this.http.get(this.get_all_blogs_url);
  }

  delete_blog(id: string) {
      return this.http.delete(this.delete_blog_url + id);
  }

  get_single_blog(blogId: string) {
    return this.http.get(this.get_single_blog_url + blogId);
  }

  update_blog(blogProbs: Object, blogId: string) {
    return this.http.put(this.update_blog_url + blogId, blogProbs);
  }
}


