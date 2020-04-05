import { BlogService } from './../api-calls/blog.service';
import { Component, OnInit } from '@angular/core';

interface Blog {
  title: string;
  feature_image: string;
  created_at: string;
  content: string;
}

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
  private allBlogs: Blog[] = [];
  constructor(private blogService: BlogService) { }

  ngOnInit() {
    this.load_all_blogs();
  }

  load_all_blogs() {
    this.blogService.get_all_blogs().subscribe((response: any) => {
      console.log(response);
      response.all_messages.forEach((element: any) => {
        this.allBlogs.push(element);
        console.log(element.name);
      });
    });
  }

}
