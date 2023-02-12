import { Component, OnInit } from '@angular/core';
import { IngredientService } from '../service/ingredient/ingredient.service';

@Component({
  selector: 'app-list-ingredient',
  templateUrl: './list-ingredient.component.html',
  styleUrls: ['./list-ingredient.component.css']
})
export class ListIngredientComponent implements OnInit {
  componentName: String;
  Ingredients: any = [];
  handleUpdateResponse: any;
  handleError: any;

  constructor(private ingredientService: IngredientService) {
    this.componentName = "ingredients";
 }
  // Angular Init method, retrieve all notifications from database
  ngOnInit(): void {
    this.ingredientService.getIngredients().subscribe(res => {
      console.log(res)
      this.Ingredients = res;
    });
  }
}