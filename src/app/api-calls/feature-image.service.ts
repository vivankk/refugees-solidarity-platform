import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FeatureImageService {
  private imgur_url = 'https://api.imgur.com/3/image';
  private client_id = '79a7401fc8016ab';
  constructor(private http: HttpClient) { }

  upload_image(image_file: File) {
    const formData = new FormData();
    formData.append('image', image_file, image_file.name);


    const headers = new HttpHeaders({
      authorization: 'Client-ID ' + this.client_id
    });

    return this.http.post(this.imgur_url , formData, {headers});
  }
}
