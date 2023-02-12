import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-recipe-card',
  template: `<div>{{qObj.question}}`,
  templateUrl: './recipe-card.component.html',
  styleUrls: ['./recipe-card.component.css']
})
export class RecipeCardComponent {
  // @Input() qObj:Object;
}
