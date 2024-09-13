import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-abm',
  templateUrl: './abm.component.html',
  styleUrl: './abm.component.css'
})
export class AbmComponent {
  @Input() user_id!: string;
  @Input() tipoOperacion!: string;
}
