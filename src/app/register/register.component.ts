import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {UserService} from '../api-calls/user.service';
import {AlertDialogBodyComponent} from '../alert-dialog-body/alert-dialog-body.component';
import {DialogBodyComponent} from '../dialog-body/dialog-body.component';
import {MatDialog} from '@angular/material/dialog';
import {FeatureImageService} from '../api-calls/feature-image.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  private selectedFile: File;
  private previewImage: any;
  private userId: string;
  private showSpinner = false;
  private hide: true;
  private typesOfSkills: string[] = ['skill1', 'skill2'];
  private skills: [];
  private firstName: string;
  private lastName: string;
  private phone: string;
  private email: string;
  private password: string;
  private userDescription: string;


  constructor(private imageService: FeatureImageService, private router: Router, private userService: UserService, private dialog: MatDialog) { }

  ngOnInit() {
  }

  processFile(imageInput: any) {
    this.selectedFile = imageInput.files[0];
    this.previewImageLoad();
  }

  previewImageLoad() {
    const reader = new FileReader();
    reader.onloadend = e => {
      this.previewImage = reader.result;
    };
    reader.readAsDataURL(this.selectedFile);
  }

  open_dialog(message: string) {
    const dialogRef = this.dialog.open(DialogBodyComponent, {
      width: '550px',
      height: '200px',
      data: {
        message
      }

    });
    dialogRef.afterClosed().subscribe((confirm: boolean) => {
      if (confirm) {
        this.submit_form();
      }
    });

  }

  open_alert_dialog(message: string) {
    const dialogRef = this.dialog.open(AlertDialogBodyComponent, {
      width: '550px',
      height: '200px',
      data: {
        message
      }
    });
  }

  async submit_form() {
    this.showSpinner = true;
    const imageData = await this.imageService.upload_image(this.selectedFile).toPromise();
    const userProbs = {
      first_name: this.firstName,
      last_name: this.lastName,
      email: this.email,
      password: this.password,
      skills: this.skills,
      photo: imageData.data.link,
      userDescription: this.userDescription
    };

    this.userService.add_user(userProbs).subscribe((response: any) => {
      this.userId = response.id;
      this.showSpinner = false;
      this.open_alert_dialog(`Blog has been created with the id: ${this.userId}`);

      this.previewImage = '';
      this.skills = [];
      this.email = '';
      this.password = '';
      this.skills = [];
      this.userDescription = '';
    });
  }


}
